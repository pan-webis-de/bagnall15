def write_answers(filename, results):
    if filename == '-':  # use stdout
        for k, v in sorted(results.items()):
            print "%s %.3f" % (k, v)
    else:
        f = open(filename, 'w')
        for k, v in sorted(results.items()):
            print >>f, "%s %.3f" % (k, v)
        f.close()


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


def scale_results(index_results):
    """invert indices and scale to 0-1"""
    results = {}
    scale = 1.0 / len(index_results)
    for k, v in index_results.items():
        results[k] = 1.0 - v * scale
    return results
