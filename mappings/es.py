# OPTIONS: threshold 1e-05, dotellipses collapse_digits decompose_caps decompose
decomposed = {
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
    u'E': u'e\xb9',             # decomposed caps 
    u'P': u'p\xb9',             # decomposed caps 
    u'\r': '',                  # dispensible
    u'x': u'x',
    u'L': u'l\xb9',             # decomposed caps 
    u'C': u'c\xb9',             # decomposed caps 
    u'\u0303': u'\u0303',       # "̃" -> "̃"  kept Mn (3882) COMBINING TILDE
    u'M': u'm\xb9',             # decomposed caps 
    u'A': u'a\xb9',             # decomposed caps 
    u'N': u'n\xb9',             # decomposed caps 
    u'\u201c': '"',             # "“" -> """  double quote LEFT DOUBLE QUOTATION MARK
    u'\u201d': '"',             # "”" -> """  double quote RIGHT DOUBLE QUOTATION MARK
    u'S': u's\xb9',             # decomposed caps 
    u'I': u'i\xb9',             # decomposed caps 
    u'1': '7',                  # digit
    u':': u':',                 # kept Po (1944)
    u'R': u'r\xb9',             # decomposed caps 
    u'G': u'g\xb9',             # decomposed caps 
    u'0': '7',                  # digit
    u'D': u'd\xb9',             # decomposed caps 
    u'T': u't\xb9',             # decomposed caps 
    u'2': '7',                  # digit
    u'H': u'h\xb9',             # decomposed caps 
    u'Y': u'y\xb9',             # decomposed caps 
    u'O': u'o\xb9',             # decomposed caps 
    u'U': u'u\xb9',             # decomposed caps 
    u'F': u'f\xb9',             # decomposed caps 
    u'\u2013': u'\u2013',       # "–" -> "–"  kept Pd (981) EN DASH
    u'\xbf': u'\xbf',           # "¿" -> "¿"  kept Po (924) INVERTED QUESTION MARK
    u'?': u'?',                 # kept Po (924)
    u'B': u'b\xb9',             # decomposed caps 
    u'(': u'(',                 # kept Ps (872)
    u')': u')',                 # kept Pe (872)
    u'\u2014': u'\u2014',       # "—" -> "—"  kept Pd (812) EM DASH
    u';': u';',                 # kept Po (743)
    u'Q': u'q\xb9',             # decomposed caps 
    u'J': u'j\xb9',             # decomposed caps 
    u'V': u'v\xb9',             # decomposed caps 
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
    u'K': u'k\xb9',             # decomposed caps 
    u'X': u'x\xb9',             # decomposed caps 
    u'7': '7',                  # digit
    u'Z': u'z\xb9',             # decomposed caps 
    u'\u2019': "'",             # "’" -> "'"  single quote RIGHT SINGLE QUOTATION MARK
    u'W': u'w\xb9',             # decomposed caps 
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
# mapping 97 characters to 53, (decomposed)
