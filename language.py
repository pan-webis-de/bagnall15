# -*- coding: utf-8 -*-
import os
import unicodedata
import re
from collections import Counter

TRAINING_FN_PATTERN = r'^known\d+\.txt$'
TEST_FN_PATTERN = r'^unknown\.txt$'

training_fn_search = re.compile(TRAINING_FN_PATTERN).search
test_fn_search = re.compile(TEST_FN_PATTERN).search


def _read_file(fn, convert, default):
    if os.path.isdir(fn):
        fn = os.path.join(fn, default)
    result = {}
    f = open(fn)
    for line in f:
        k, v = line.strip().split()
        k = re.sub(r'\W', '', k)  # possible \uFEFF on first line
        result[k] = convert(v)
    f.close()
    return result


def read_truth_file(truth_file):
    return _read_file(truth_file, 'Y'.__eq__, 'truth.txt')


def read_answers_file(fn):
    return _read_file(fn, float, 'answers.txt')


def always(x):
    return True


def load_texts(srcdir, remap,
               class_accept=always,
               file_accept=training_fn_search,
               reverse=False):
    texts = {}
    for subdir in os.listdir(srcdir):
        if not class_accept(subdir):
            continue
        full_subdir = os.path.join(srcdir, subdir)
        if not os.path.isdir(full_subdir):
            continue
        for fn in os.listdir(full_subdir):
            if file_accept(fn):
                ffn = os.path.join(full_subdir, fn)
                f = open(ffn)
                text = remap(f.read())
                texts.setdefault(subdir, []).append(text)
                f.close()
    return texts


def load_corpus_map(srcdir, remap, exclude_test=False):
    accept = training_fn_search if exclude_test else always
    return load_texts(srcdir, remap, file_accept=accept)


def load_corpus(srcdir, remap, exclude_test=False):
    texts = load_corpus_map(srcdir, remap, exclude_test)
    all_texts = []
    for v in texts.values():
        all_texts.extend(v)
    return all_texts


def concat_corpus(srcdir, remap, exclude_test=False):
    all_texts = load_corpus(srcdir, remap, exclude_test)
    return '\n'.join(all_texts)


def count_chars(text, decompose=False):
    text = text.decode('utf-8')
    if decompose:
        text = unicodedata.normalize('NFKD', text)
    else:
        text = unicodedata.normalize('NFKC', text)
    c = Counter(text)
    return c.most_common()


dispensible_chars = set('\x0b\x0c\r'.decode('utf8') + u'\ufeff\xad\x85' +
                        u'\u2028\\_+')

single_quotes = set("'‘’‘‘".decode('utf8') + u'\u2018')

double_quotes = set('‟"„“”'.decode('utf8'))


def unify_case(text):
    # trickier than .lower() because of the decomposed case marker
    text = text.lower()
    return text.replace("¹".decode('utf8'), "")


def split_words(text, ignore_case=False):
    if not isinstance(text, unicode):
        text = text.decode('utf8')
    if ignore_case:
        text = unify_case(text)
    text = re.sub(r"(?<=\w)'(?=\w)", r"³".decode('utf8'),
                  text, flags=re.U)
    words = re.split(r"[^\w³-]+".decode('utf8'), text, flags=re.U)
    words = sum((w.split('--') for w in words), [])
    words = [x.strip('-_') for x in words]
    return [x for x in words if x]


def decode_split_word(w):
    return w.replace('³'.decode('utf8'), "'")


def print_word_counts(c):
    prev_n = None
    for w, n in c.most_common():
        if n != prev_n:
            print "\n------------- %s --------------" % n
            prev_n = n
        w = decode_split_word(w)
        print w,
    print
    print len(c)

LANG_CODES = ('DU', 'SP', 'EN', 'GR')

def guess_directory_lang(d):
    for subdir in os.listdir(d):
        if not os.path.isdir(os.path.join(d, subdir)):
            continue
        key = subdir[:2]
        if key in LANG_CODES and subdir[2:].isdigit():
            return key
