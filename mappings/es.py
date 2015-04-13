# -*- coding: utf-8 -*-
# OPTIONS: threshold 1e-05, dotellipses collapse_brackets collapse_dashes collapse_digits decompose_caps decompose
charmap = {
    u' ': u' ',                 # kept Zs (471317)
    u'e': u'e',
    u'a': u'a',
    u'o': u'o',
    u's': u's',
    u'n': u'n',
    u'i': u'i',
    u'r': u'r',
    u'l': u'l',
    u'd': u'd',
    u'c': u'c',
    u't': u't',
    u'u': u'u',
    u'm': u'm',
    u'p': u'p',
    u'\u0301': u'\u0301',       # "́" -> "́"  kept Mn (47049) COMBINING ACUTE ACCENT
    u',': u',',                 # kept Po (30278)
    u'b': u'b',
    u'g': u'g',
    u'q': u'q',
    u'v': u'v',
    u'.': u'.',                 # kept Po (22020)
    u'y': u'y',
    u'f': u'f',
    u'h': u'h',
    u'z': u'z',
    u'j': u'j',
    u'\n': u'\n',               # kept Cc (5858)
    u'E': u'\xb9e',             # decomposed caps
    u'P': u'\xb9p',             # decomposed caps
    u'\r': '',                  # dispensible
    u'x': u'x',
    u'L': u'\xb9l',             # decomposed caps
    u'C': u'\xb9c',             # decomposed caps
    u'\u0303': u'\u0303',       # "̃" -> "̃"  kept Mn (3882) COMBINING TILDE
    u'M': u'\xb9m',             # decomposed caps
    u'A': u'\xb9a',             # decomposed caps
    u'N': u'\xb9n',             # decomposed caps
    u'\u201c': '"',             # "“" -> """  double quote LEFT DOUBLE QUOTATION MARK
    u'\u201d': '"',             # "”" -> """  double quote RIGHT DOUBLE QUOTATION MARK
    u'S': u'\xb9s',             # decomposed caps
    u'I': u'\xb9i',             # decomposed caps
    u'1': '7',                  # digit
    u':': u':',                 # kept Po (1944)
    u'R': u'\xb9r',             # decomposed caps
    u'G': u'\xb9g',             # decomposed caps
    u'0': '7',                  # digit
    u'D': u'\xb9d',             # decomposed caps
    u'T': u'\xb9t',             # decomposed caps
    u'2': '7',                  # digit
    u'H': u'\xb9h',             # decomposed caps
    u'Y': u'\xb9y',             # decomposed caps
    u'O': u'\xb9o',             # decomposed caps
    u'U': u'\xb9u',             # decomposed caps
    u'F': u'\xb9f',             # decomposed caps
    u'\u2013': u'\u2014',       # "–" -> "—"  unified dash EN DASH
    u'\xbf': u'\xbf',           # "¿" -> "¿"  kept Po (924) INVERTED QUESTION MARK
    u'?': u'?',                 # kept Po (924)
    u'B': u'\xb9b',             # decomposed caps
    u'(': u'(',                 # kept Ps (872)
    u')': u')',                 # kept Pe (872)
    u'\u2014': u'\u2014',       # "—" -> "—"  unified dash EM DASH
    u';': u';',                 # kept Po (743)
    u'Q': u'\xb9q',             # decomposed caps
    u'J': u'\xb9j',             # decomposed caps
    u'V': u'\xb9v',             # decomposed caps
    u'4': '7',                  # digit
    u'6': '7',                  # digit
    u'\ufeff': '',              # "﻿" -> ""  dispensible ZERO WIDTH NO-BREAK SPACE
    u'3': '7',                  # digit
    u'9': '7',                  # digit
    u'k': u'k',
    u'-': u'-',                 # kept Pd (387)
    u'5': '7',                  # digit
    u'"': '"',                  # double quote
    u'8': '7',                  # digit
    u'/': u'/',                 # kept Po (352)
    u'w': u'w',
    u'K': u'\xb9k',             # decomposed caps
    u'X': u'\xb9x',             # decomposed caps
    u'7': '7',                  # digit
    u'Z': u'\xb9z',             # decomposed caps
    u'\u2019': "'",             # "’" -> "'"  single quote RIGHT SINGLE QUOTATION MARK
    u'W': u'\xb9w',             # decomposed caps
    u'%': u'%',                 # kept Po (130)
    u'!': u'!',                 # kept Po (95)
    u'\xab': u'\xab',           # "«" -> "«"  kept Pi (54) LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\xbb': u'\xbb',           # "»" -> "»"  kept Pf (54) RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\xad': '',                # "­" -> ""   dispensible SOFT HYPHEN
    u'\xa1': u'\xa1',           # "¡" -> "¡"  kept Po (51) INVERTED EXCLAMATION MARK
    u'\u2018': "'",             # "‘" -> "'"  single quote LEFT SINGLE QUOTATION MARK
    u'@': u'@',                 # kept Po (41)
    u'\u0308': u'\u0308',       # "̈" -> "̈"  kept Mn (41) COMBINING DIAERESIS
    u'#': '',                   # removed Po, 20 < 29
    u'\u0327': '',              # "̧" -> ""   removed Mn, 15 < 29 COMBINING CEDILLA
    u"'": "'",                  # single quote
    u'*': '',                   # removed Po, 2 < 29
}
# mapping 97 characters to 52, (decomposed)
