# -*- coding: utf-8 -*-
import glob
from collections import defaultdict
import re
from language import read_answers_file
import itertools
import random
import subprocess
import os
from colour import get_namespace


def set_use_colour(use_colour):
    global colour
    colour = get_namespace(use_colour)
    return colour


def simple_file_gen(file_pattern):
    for fn in glob.glob(file_pattern):
        yield fn


# presynaptic noise was broken until c34d2535
def does_psn_work(commit_id):
    try:
        f = open(os.devnull, 'w')
        s = subprocess.check_output(['git', 'rev-list', '--count',
                                     'c34d25351..%s' % commit_id],
                                    stderr=f)
        f.close()
        return int(s)
    except subprocess.CalledProcessError:
        #directories with no commit are newer.
        return True


def prune_config(config, commit):
    pruned = []
    skip = 0
    flags = set()
    for x in config:
        if skip:
            skip -= 1
            continue
        if x in {'-M', '-n', '--pan-answers', '--raw-answers',
                 '--raw-answers-trace', '--control-corpus'}:
            skip = 1
            flags.add(x)
            continue
        if x in {'-r8', '--pan-hedge=0.0', '--try-swapping-texts',
                 '--activation=2', '--learning-method=4',
                 '--ignore-start=10', '--batch-size=40', '-d70'}:
            continue
        if x.startswith('corpus/pan15-authorship-verification-training-data'):
            continue

        if (x.startswith('--presynaptic-noise=') and
            not does_psn_work(commit)):
            continue

        pruned.append(x)

    if '--control-corpus' not in flags:
        pruned.append("%s--no-control-corpus%s" % (colour.RED, colour.C_NORMAL))

    return pruned


def fix_config_epoch(orig_cmdline, epoch):
    cmdline = orig_cmdline[:]
    for i, x in enumerate(cmdline):
        if x[:2] == '-e':
            if len(x) == 2:
                cmdline[i] = '-e'
                cmdline[i + 1] = '%s' % epoch
            if len(x) > 2:
                cmdline[i] = '-e%s' % epoch
            break
    return cmdline


def read_config(fn):
    f = open(fn)
    for line in f:
        if line.startswith('running ./train-net'):
            break
    else:
        f.close()
        return None
    f.close()
    commit = get_shortname(fn)
    config = line.split()[2:]
    for x in config:
        if 'pan15-authorship-verification-training-dataset-' in x:
            date = x[-10:]
            version = {'2015-03-02': 3,
                       '2015-04-19': 4}.get(date)
    return commit, version, config


def read_config_from_shortname(lang, name):
    if '-' in name:
        name = name[:name.index('-')]
    fn = 'answers-%s/stderr-%s.log' % (name, lang)
    return read_config(fn)

# corpus changed in early may. I'm calling them versions 3 and 4
# because those appear in the filenames. (as months)
_version_cache = {}
def uses_corpus_version(n, path):
    dirname, lang = os.path.split(os.path.dirname(path))
    version = _version_cache.get(dirname)
    if version is None:
        try:
            fn = '%s/stderr-%s.log' % (dirname, lang)
            f = open(fn)
            for line in f:
                if line[:7] == 'running':
                    m = re.search(r'2015-0(\d)-\d\d', line)
                    if m:
                        version = int(m.group(1))
                    break
            _version_cache[dirname] = version
        except IOError, e:
            print e
    return version == n


def versioned_file_gen(file_pattern, version):
    for fn in glob.glob(file_pattern):
        if uses_corpus_version(version, fn):
            yield fn


def always(x):
    return True


def never(x):
    return False


def regex_filter(regex):
    if regex is None:
        return always
    return re.compile(regex).search


def get_roc_trail(answers, truth):
    rmap = {}
    for k, v in answers.items():
        t = truth[k]
        r = rmap.setdefault(v, [0, 0])
        r[0] += t
        r[1] += not t
    trail = [(score, d[0], d[1])
             for score, d in sorted(rmap.items())]
    n_true = sum(truth.values())
    n_false = len(truth) - n_true
    return trail, n_true, n_false


def calc_auc_from_trail(roc_trail, n_true, n_false):
    true_positives, false_positives = n_true, n_false
    tp_scale = 1.0 / (n_true or 1)
    fp_scale = 1.0 / (n_false or 1)
    px, py = 1, 1  # previous position for area calculation
    auc = 1.0

    for score, positives, negatives in roc_trail:
        false_positives -= negatives
        true_positives -= positives
        x = false_positives * fp_scale
        y = true_positives * tp_scale
        auc += (px + x) * 0.5 * (y - py)
        px = x
        py = y

    auc += px * 0.5 * -py  # is this ever necesssary?
    return auc


def calc_auc(answers, truth):
    results, n_true, n_false = get_roc_trail(answers, truth)
    return calc_auc_from_trail(results, n_true, n_false)


def calc_cat1(answers, truth):
    # (1/n)*(nc+(nu*nc/n))
    n_correct = 0
    n_undecided = 0
    n = len(answers)
    for k, v in answers.items():
        if v == 0.5:
            n_undecided += 1
        else:
            n_correct += (v > 0.5) == truth[k]

    scale = 1.0 / n
    return (n_correct + n_undecided * n_correct * scale) * scale


def print_candidate(b, c='', prefix='best', fn=''):
    if fn:
        fn = "%20s" % fn
    print ("%s%9s %s auc*cat1 %.4f; cat1 %.3f; auc %.3f; range (%d-%d) "
           "(%.3f - %.3f) undecided %2d; correct %2d tp %2d tf %2d" %
           ((c, prefix, fn) + b) + colour.C_NORMAL)


def split_roc_trail(orig_trail, s, e):
    head = orig_trail[:s]
    middle = orig_trail[s:e]
    target = orig_trail[e]
    score_e = target[0]
    if middle:
        score_s = middle[0][0]
    else:
        score_s = score_e

    tail = orig_trail[e + 1:]
    score, positives, negatives = target
    for _, p, n in middle:
        positives += p
        negatives += n
    return head, [(score, positives, negatives)], tail, score_s, score_e


def evaluate_fixed_cat1(answers, truth, cat1_centre, cat1_radius=0):
    roc_trail, n_true, n_false = get_roc_trail(answers, truth)
    cat1_bottom = cat1_centre - cat1_radius
    cat1_top = cat1_centre + cat1_radius

    s = None
    for i, x in enumerate(roc_trail):
        score, u_pos, u_neg = x
        if s is None and score > cat1_bottom:
            s = i
        if score > cat1_top:
            break
    e = max(s, i)

    head, middle, tail, score_s, score_e = split_roc_trail(roc_trail, s, e)
    auc = calc_auc_from_trail(head + middle + tail, n_true, n_false)
    score, u_pos, u_neg = middle[0]
    n_undecided = u_pos + u_neg
    n_tp = sum(x[1] for x in tail)
    n_tf = sum(x[2] for x in head)
    n_correct = n_tp + n_tf
    scale = 1.0 / len(truth)
    cat1 = (n_correct + n_undecided * n_correct * scale) * scale
    candidate = (cat1 * auc, cat1, auc, s, e, cat1_bottom, cat1_top,
                 n_undecided, n_correct, n_tp, n_tf)

    return candidate, roc_trail, auc


def search_for_centre(answers, truth):
    roc_trail, n_true, n_false = get_roc_trail(answers, truth)

    auc = calc_auc_from_trail(roc_trail, n_true, n_false)

    # at bottom end of scale
    true_positives = n_true
    true_negatives = 0
    scale = 1.0 / len(truth)
    best_candidate = (0,)

    for i, roc_data in enumerate(roc_trail):
        raw_score, positives, negatives = roc_data
        true_positives -= positives
        n_undecided = positives + negatives
        n_correct = true_positives + true_negatives
        cat1 = (n_correct + n_undecided * n_correct * scale) * scale
        score = cat1 * auc
        if score > best_candidate[0]:
            best_candidate = (score, cat1, auc, i, i, raw_score, raw_score,
                              n_undecided, n_correct, true_positives,
                              true_negatives)
        true_negatives += negatives
    return best_candidate, roc_trail, auc


def search(answers, truth, verbose=False):
    if verbose:
        print "searching around"
        print_c = print_candidate
    else:
        def print_c(*args, **kwargs):
            pass

    best_candidate, roc_trail, auc = search_for_centre(answers, truth)
    indicators = {'centre': best_candidate}
    median_answers = balance_results(answers)
    median_candidate = evaluate_fixed_cat1(median_answers, truth, 0.5, 0)[0]
    #print median_candidate
    indicators['median'] = median_candidate
    centre = best_candidate[3]
    print_c(best_candidate)

    index_keys = (0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75)
    indices = {k: 0 for k in index_keys}
    for i, x in enumerate(roc_trail):
        score, u_pos, u_neg = x
        for k, v in indices.items():
            if score <= k:
                indices[k] = i

    rindices = {v: k for k, v in indices.items()}

    default_cat1 = calc_cat1(answers, truth)
    default_score = auc * default_cat1

    scale = 1.0 / len(truth)
    n_true = sum(truth.values())
    n_false = len(truth) - n_true

    min_s = min(max(centre - 20, 0), indices[0.45])
    max_s = max(min(centre + 20, len(roc_trail)), indices[0.75])
    for s in range(min_s, max_s):
        for e in range(s, max_s):
            head, middle, tail, score_s, score_e = split_roc_trail(roc_trail,
                                                                   s, e)
            auc = calc_auc_from_trail(head + middle + tail, n_true, n_false)
            score, u_pos, u_neg = middle[0]
            n_undecided = u_pos + u_neg
            n_tp = sum(x[1] for x in tail)
            n_tf = sum(x[2] for x in head)
            n_correct = n_tp + n_tf
            cat1 = (n_correct + n_undecided * n_correct * scale) * scale
            candidate = (cat1 * auc, cat1, auc, s, e, score_s, score_e,
                         n_undecided, n_correct, n_tp, n_tf)
            if candidate > best_candidate:
                best_candidate = candidate
                print_c(candidate)
                indicators['range'] = candidate
            if s in rindices and e in rindices:
                if candidate > indicators['centre']:
                    c = colour.GREEN
                elif candidate[0] > default_score:
                    c = colour.YELLOW
                else:
                    c = colour.RED
                if s != e:
                    name = '%d-%d' % (rindices[s] * 100, rindices[e] * 100)
                else:
                    name = '%d' % (rindices[s] * 100,)
                print_c(candidate, c, prefix=name)
                indicators[name] = candidate

    return indicators


def get_shortname(fn, epoch_from_filename=False):
    m = re.search(r'answers-([^/]+)/[^\d]+(\d+)?', fn)
    if m:
        shortname = m.group(1)
        if epoch_from_filename:
            shortname = '%s-%s' % (shortname, m.group(2))
    else:
        shortname = fn
    return shortname

def answers_generator(filename_gen, truth, epoch_from_filename=False,
                 use_shortname=True):
    for fn in filename_gen:
        answers = read_answers_file(fn)
        if use_shortname:
            fn = get_shortname(fn, epoch_from_filename)
        yield (fn, answers)

    results = defaultdict(list)


def get_indicators(answers_iter, truth):
    #XXX auto-truth?
    results = defaultdict(list)
    for fn, answers in answers_iter:
        indicators = search(answers, truth)
        for k, v in indicators.items():
            results[k].append((v, fn))
    return results


def _find_winners(results):
    winners = []
    for k, v in sorted(results.items()):
        v.sort()
        v.reverse()
        winners.append((v[0][0], v[0][1], k))
    return winners


def get_indicator_scores(results):
    totals = {}
    for x in results.values():
        for candidate, fn in x:
            t = totals.setdefault(fn, [0.0, 0])
            t[0] += candidate[0]
            t[1] += 1

    top_scores = sorted((v[0] / v[1], k) for k, v in totals.items())
    top_scores.reverse()
    return top_scores


def get_sorted_scores(answers_gen, truth, cat1_centre=None, cat1_radius=0,
                      exclude=None, epoch_from_filename=False):
    scores = []
    for fn, answers in answers_gen:
        if exclude and exclude(fn):
            continue
        if cat1_centre is not None:
            s = evaluate_fixed_cat1(answers, truth, cat1_centre, cat1_radius)
        else:
            s = search_for_centre(answers, truth)
        scores.append((s[0], fn, get_shortname(fn, epoch_from_filename)))
    scores.sort()
    scores.reverse()
    return scores


def search_answer_files(filename_gen, truth, epoch_from_filename=False):

    answers_gen = answers_generator(filename_gen, truth,
                                    epoch_from_filename)
    results = get_indicators(answers_gen, truth)

    winners = _find_winners(results)
    best = max(c[0] for c, n, k in winners if not k.isalpha())
    near = best * 0.99
    for candidate, name, key in winners:
        if key.isalpha():
            c = colour.CYAN
        elif candidate[0] == best:
            c = colour.YELLOW
        elif candidate[0] > near:
            c = colour.MAGENTA
        else:
            c = ''
        print_candidate(candidate, c, prefix=key, fn=name)

    top_scores = get_indicator_scores(results)

    colour_map = {t[1]: c for c, t
                  in zip(colour.SPECTRUM, top_scores)}

    for score, name in top_scores:
        print "%s%s %.3f%s" % (colour_map.get(name, ''), name, score,
                               colour.C_NORMAL),
    print
    notable_commits = set(x[1] for x in top_scores[:5])
    for k, v in sorted(results.items()):
        print "%8s" % k,
        notable_commits.add(v[0][1])
        for candidate, fn in v[:10]:
            print "%s%s %.3f%s" % (colour_map.get(fn, ''), fn, candidate[0],
                                   colour.C_NORMAL),
        print

    for name in notable_commits:
        print "%s%s%s" % (colour_map.get(name, ''), name,
                          colour.C_NORMAL),
    print


def search_commits(filename_gen, truth, n=8, epoch_from_filename=False,
                   cat1_centre=None, cat1_radius=0):
    answers_gen = answers_generator(filename_gen, truth,
                                    epoch_from_filename,
                                    use_shortname)
    if cat1_generator is None:
        results = get_indicators(answers_gen, truth)
        scores = get_indicator_scores(results)
        notable_commits = set(x[1] for x in scores[:n])
        for v in results.values():
            notable_commits.add(v[0][1])

    else:
        notable_commits = (x[2] for x in
                           get_sorted_scores(answers_gen, truth))

    for name in notable_commits:
        print name


def search_one(answers, truth, verbose=False):
    indicators = search(answers, truth, verbose=verbose)
    best = max(v[0] for k, v in indicators.items() if not k.isalpha())
    near = best * 0.99
    for k, v in sorted(indicators.items()):
        if k.isalpha():
            c = colour.CYAN
        elif v[0] == best:
            c = colour.YELLOW
        elif v[0] > near:
            c = colour.MAGENTA
        else:
            c = ''
        print_candidate(v, c, prefix=k)
    return indicators


def generate_ensembles(filename_gen, ensemble_size, truth,
                       sample_size=14, replace=False, randomise=False,
                       epoch_from_filename=False,
                       cat1_centre=None, cat1_radius=0,
                       include=always, exclude=never, iterations=1):
    answers_gen = answers_generator(filename_gen, truth,
                                    epoch_from_filename, False)

    scores = get_sorted_scores(answers_gen, truth, cat1_centre, cat1_radius,
                               exclude, epoch_from_filename=epoch_from_filename)
    results = []

    for i in range(iterations):
        if randomise:
            random.shuffle(scores)
        cutoff = sample_size
        singles = {}
        essentials = set()
        single_lines = []
        if include is not always:
            for c, fn, shortname in scores:
                if include(shortname):
                    singles[shortname] = read_answers_file(fn)
                    cutoff -= 1
                    single_lines.append((c[0], shortname))
                    essentials.add(shortname)

        if cutoff < 0:
            cutoff = 0

        for c, fn, shortname in scores[:cutoff]:
            singles[shortname] = read_answers_file(fn)
            single_lines.append((c[0], shortname))

        ensembles = []
        if replace:
            combos = itertools.combinations_with_replacement
        else:
            combos = itertools.combinations

        for names in combos(singles.keys(), ensemble_size):
            ensemble = {}
            if essentials and not essentials.intersection(names):
                continue

            for n in names:
                answers = singles.get(n)
                for k, v in answers.items():
                    score = ensemble.get(k, 0.0)
                    ensemble[k] = score + v
            for k, v in ensemble.items():
                ensemble[k] = v / ensemble_size

            if cat1_centre is None:
                centre = search_for_centre(ensemble, truth)
            else:
                centre = evaluate_fixed_cat1(ensemble, truth, cat1_centre,
                                             cat1_radius)

            ensembles.append((centre[0], names))

        ensembles.sort()
        results.append((single_lines, singles, ensembles))

    return results

def get_colour_spectrum(names):
    n_pattern = '%%s%%-%ds%%s' % max(len(x) for x in names)
    cstep = len(colour.SPECTRUM) / len(names)
    spectrum = (x for i, x in enumerate(colour.SPECTRUM) if not i % cstep)
    coloured = {k: n_pattern % (v, k, colour.C_NORMAL) for k, v in
                zip(names, spectrum)}
    return coloured


def calc_ensemble_usefulness(singles, ensembles):
    counts = {k: 0 for k in singles}
    scores = {k: 0.0 for k in singles}
    overall_score = 0.0
    for score, names in ensembles:
        overall_score += score[0]
        for name in names:
            counts[name] += 1
            scores[name] += score[0]

    mean_score = overall_score / len(ensembles)
    deltas = {}
    for name, score in sorted(scores.items()):
        deltas[name] = score / counts[name] - mean_score
    return deltas


def print_ensemble_usefulness(ensemble_data, lang, n_results=0):
    print lang
    delta_sums = defaultdict(float)
    delta_counts = defaultdict(int)
    score_map = {}
    for single_lines, singles, ensembles in ensemble_data:
        deltas = calc_ensemble_usefulness(singles, ensembles)
        for k, v in deltas.items():
            delta_sums[k] += v
            delta_counts[k] += 1

        coloured = get_colour_spectrum(deltas.keys())
        if len(ensemble_data) == 1:
            for name, delta in sorted(deltas.items(), key=lambda x: x[1]):
                print "%s %+.3f" % (coloured[name], delta)
        score_map.update((k, v) for v, k in single_lines)


    if len(ensemble_data) > 1:
        print "RESULTS"
        delta_means = []
        for k, v in delta_sums.items():
            c = delta_counts[k]
            delta_means.append((v / c, c, k))

        for score, count, name in sorted(delta_means)[-n_results:]:
            config = read_config_from_shortname(lang, name)
            if '-' in name:
                commit, epoch = name.split('-', 1)
                cmdline = fix_config_epoch(config[2], epoch)
                cmdline = prune_config(cmdline, commit)
            else:
                cmdline = prune_config(cmdline, name)

            single_score = score_map.get(name, '')
            print "%12s %s%.3f%s %2d %+.3f %s%s%s" % (name,
                                                      colour.GREY,
                                                      single_score,
                                                      colour.C_NORMAL,
                                                      count, score,
                                                      colour.GREY,
                                                      ' '.join(cmdline),
                                                      colour.C_NORMAL)


def print_ensembles(single_lines, singles, ensembles, n_results=0):
    coloured = get_colour_spectrum(singles.keys())

    prev = None
    for score, shortname in sorted(single_lines):
        if shortname != prev:
            print "%s %.3f" % (coloured[shortname], score)
            prev = shortname

    centre_sum = 0.0
    centre_sum2 = 0.0
    for i, x in enumerate(ensembles[-n_results:]):
        c, names = x
        name = '|'.join(coloured[x] for x in names)
        n = len(set(names))
        if n == 1:
            _colour = colour.RED
        elif n < len(names):
            _colour = colour.YELLOW
        else:
            _colour = colour.C_NORMAL
        if i == len(ensembles) // 2:
            _colour = colour.MAGENTA
        centre = (c[5] + c[6]) * 0.5
        centre_sum += centre
        centre_sum2 += centre * centre

        print "%s%s %.3f auc %.3f c@1 %.3f centre %.2f%s" % (name,
                                                             _colour,
                                                             c[0], c[2], c[1],
                                                             centre,
                                                             colour.C_NORMAL)
    n = max(1, len(ensembles))

    centre_mean = centre_sum / n
    centre_dev = max(0, (centre_sum2 / n -
                         centre_mean * centre_mean)) ** 0.5
    print "%scentre %.3f±%.3f%s" % (colour.YELLOW, centre_mean, centre_dev,
                                    colour.C_NORMAL)


def balance_results(results, cat1_centre=None, cat1_radius=0):
    ordered_results = [(v, k) for k, v in results.items()]
    ordered_results.sort()
    ordered_results.reverse()
    if cat1_centre is None:
        m1 = (len(results) - 1) // 2
        m2 = len(results) // 2
        cat1_centre = (ordered_results[m1][0] +
                       ordered_results[m2][0]) * 0.5

    cat1_top = min(cat1_centre + cat1_radius, 0.99)
    cat1_bottom = max(cat1_centre - cat1_radius, 0.01)

    cat1_top_scale = 0.5 / (1.0 - cat1_top)
    cat1_bottom_scale = 0.5 / cat1_bottom

    scaled_results = {}
    for score, k in ordered_results:
        if score > cat1_top:
            s = 0.5 + (score - cat1_top) * cat1_top_scale
        elif score < cat1_bottom:
            s = 0.5 + (score - cat1_bottom) * cat1_bottom_scale
        else:
            s = 0.5
        scaled_results[k] = s

    return scaled_results
