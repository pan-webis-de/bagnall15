# -*- coding: utf-8 -*-
import os
import sys
import unicodedata
import re
from collections import Counter

TRAINING_FN_PATTERN = r'^known\d+\.txt$'
TEST_FN_PATTERN = r'^unknown\.txt$'

training_fn_search = re.compile(TRAINING_FN_PATTERN).search
test_fn_search = re.compile(TRAINING_FN_PATTERN).search


def always(x):
    return True

#XXX assumes NFKD norm
def remap_text(text, charmap):
    text = text.decode('utf8')
    text = unicodedata.normalize('NFKD', text)
    return ''.join(charmap(x) for x in text).encode('utf8')


def load_texts(srcdir, class_accept=always, file_accept=training_fn_search,
               charmap=None):
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
                text = f.read()
                if charmap:
                    text = remap_text(text, charmap)
                texts.setdefault(subdir, []).append(text)
                f.close()
    return texts


def concat_corpus(srcdir, exclude_test=False):
    accept = training_fn_search if exclude_test else always
    texts = load_texts(srcdir, file_accept=accept)
    all_texts = []
    for v in texts.values():
        all_texts.extend(v)
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
                        u'\u2028')

single_quotes = set("'‘’‘‘".decode('utf8') + u'\u2018')

double_quotes = set('‟"„“”'.decode('utf8'))
