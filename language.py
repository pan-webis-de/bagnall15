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

def load_texts(srcdir, class_accept=always, file_accept=training_fn_search):
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
                texts.setdefault(subdir, []).append(f.read())
                f.close()
    return texts


def concat_corpus(srcdir, exclude_test=False):
    accept = training_fn_search if exclude_test else always
    texts = load_texts(srcdir, file_accept=accept)
    all_texts = []
    for v in texts.values():
        all_texts.extend(v)
    return ''.join(all_texts)

def count_chars(text):
    c = Counter(text.decode('utf-8'))
    return c.most_common()

def fix_en_chars():
    pass