# -*- coding: utf-8 -*-
# OPTIONS: threshold 1e-05, dotellipses collapse_brackets collapse_dashes collapse_digits decompose_caps decompose
charmap = {
    u' ': u' ',                 # kept Zs (92447)
    u'e': u'e',
    u't': u't',
    u'o': u'o',
    u'a': u'a',
    u'n': u'n',
    u'i': u'i',
    u's': u's',
    u'h': u'h',
    u'r': u'r',
    u'\n': u'\n',               # kept Cc (13082)
    u'l': u'l',
    u'd': u'd',
    u'u': u'u',
    u'y': u'y',
    u'm': u'm',
    u'g': u'g',
    u'w': u'w',
    u',': u',',                 # kept Po (5250)
    u"'": "'",                  # single quote
    u'.': u'.',                 # kept Po (4826)
    u'f': u'f',
    u'c': u'c',
    u'b': u'b',
    u'p': u'p',
    u'-': u'-',                 # kept Pd (3253)
    u'k': u'k',
    u'I': u'\xb9i',             # decomposed caps
    u'v': u'v',
    u'!': u'!',                 # kept Po (1901)
    u'A': u'\xb9a',             # decomposed caps
    u'?': u'?',                 # kept Po (1336)
    u'T': u'\xb9t',             # decomposed caps
    u'W': u'\xb9w',             # decomposed caps
    u'S': u'\xb9s',             # decomposed caps
    u'H': u'\xb9h',             # decomposed caps
    u'M': u'\xb9m',             # decomposed caps
    u'Y': u'\xb9y',             # decomposed caps
    u'B': u'\xb9b',             # decomposed caps
    u'O': u'\xb9o',             # decomposed caps
    u'C': u'\xb9c',             # decomposed caps
    u'D': u'\xb9d',             # decomposed caps
    u'N': u'\xb9n',             # decomposed caps
    u'G': u'\xb9g',             # decomposed caps
    u';': u';',                 # kept Po (313)
    u'L': u'\xb9l',             # decomposed caps
    u'j': u'j',
    u'P': u'\xb9p',             # decomposed caps
    u'F': u'\xb9f',             # decomposed caps
    u'q': u'q',
    u'E': u'\xb9e',             # decomposed caps
    u'\t': '  ',                # tab
    u'x': u'x',
    u'R': u'\xb9r',             # decomposed caps
    u'"': '"',                  # double quote
    u'J': u'\xb9j',             # decomposed caps
    u'z': u'z',
    u'V': u'\xb9v',             # decomposed caps
    u'K': u'\xb9k',             # decomposed caps
    u'Q': u'\xb9q',             # decomposed caps
    u'U': u'\xb9u',             # decomposed caps
    u'_': '',                   # dispensible
    u':': u':',                 # kept Po (40)
    u'[': u'(',                 # brackets
    u'(': u'(',                 # kept Ps (23)
    u')': u')',                 # kept Pe (21)
    u']': u')',                 # brackets
    u'}': u')',                 # brackets
    u'{': u'(',                 # brackets
    u'\\': '',                  # dispensible
    u'\u0300': '',              # "̀" -> ""   removed Mn, 2 < 3 COMBINING GRAVE ACCENT
    u'Z': u'\xb9z',             # decomposed caps kept letter under threshold 2 < 3
}
# mapping 72 characters to 40, (decomposed)
