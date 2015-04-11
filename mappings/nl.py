# OPTIONS: threshold 1e-05, dotellipses collapse_digits decompose_caps decompose
decomposed = {
    u' ': u' ',                 # kept Zs (106932)
    u'e': u'e',
    u'n': u'n',
    u'a': u'a',
    u'i': u'i',
    u't': u't',
    u'o': u'o',
    u'r': u'r',
    u'd': u'd',
    u'l': u'l',
    u's': u's',
    u'g': u'g',
    u'k': u'k',
    u'v': u'v',
    u'm': u'm',
    u'h': u'h',
    u'u': u'u',
    u'j': u'j',
    u'w': u'w',
    u'b': u'b',
    u'p': u'p',
    u'z': u'z',
    u'c': u'c',
    u'.': u'.',                 # kept Po (6000)
    u'f': u'f',
    u',': u',',                 # kept Po (3025)
    u'D': u'd\xb9',             # decomposed caps 
    u'H': u'h\xb9',             # decomposed caps 
    u'E': u'e\xb9',             # decomposed caps 
    u'V': u'v\xb9',             # decomposed caps 
    u'y': u'y',
    u"'": "'",                  # single quote
    u'2': '7',                  # digit
    u'A': u'a\xb9',             # decomposed caps 
    u'0': '7',                  # digit
    u'B': u'b\xb9',             # decomposed caps 
    u'M': u'm\xb9',             # decomposed caps 
    u'1': '7',                  # digit
    u'I': u'i\xb9',             # decomposed caps 
    u'-': u'-',                 # kept Pd (434)
    u'W': u'w\xb9',             # decomposed caps 
    u'S': u's\xb9',             # decomposed caps 
    u')': u')',                 # kept Pe (388)
    u'(': u'(',                 # kept Ps (385)
    u'O': u'o\xb9',             # decomposed caps 
    u'N': u'n\xb9',             # decomposed caps 
    u'Z': u'z\xb9',             # decomposed caps 
    u'\u0308': u'\u0308',       # "̈" -> "̈"  kept Mn (331) COMBINING DIAERESIS
    u'T': u't\xb9',             # decomposed caps 
    u'?': u'?',                 # kept Po (317)
    u':': u':',                 # kept Po (306)
    u'\ufeff': '',              # "﻿" -> ""  dispensible ZERO WIDTH NO-BREAK SPACE
    u'\n': u'\n',               # kept Cc (275)
    u'\u2019': "'",             # "’" -> "'"  single quote RIGHT SINGLE QUOTATION MARK
    u'x': u'x',
    u'\u0301': u'\u0301',       # "́" -> "́"  kept Mn (223) COMBINING ACUTE ACCENT
    u'\u2018': "'",             # "‘" -> "'"  single quote LEFT SINGLE QUOTATION MARK
    u'G': u'g\xb9',             # decomposed caps 
    u'9': '7',                  # digit
    u'3': '7',                  # digit
    u'L': u'l\xb9',             # decomposed caps 
    u'C': u'c\xb9',             # decomposed caps 
    u'4': '7',                  # digit
    u'P': u'p\xb9',             # decomposed caps 
    u'5': '7',                  # digit
    u'q': u'q',
    u'"': '"',                  # double quote
    u'R': u'r\xb9',             # decomposed caps 
    u'K': u'k\xb9',             # decomposed caps 
    u'8': '7',                  # digit
    u'J': u'j\xb9',             # decomposed caps 
    u'6': '7',                  # digit
    u'!': u'!',                 # kept Po (87)
    u'F': u'f\xb9',             # decomposed caps 
    u';': u';',                 # kept Po (80)
    u'\u201d': '"',             # "”" -> """  double quote RIGHT DOUBLE QUOTATION MARK
    u'U': u'u\xb9',             # decomposed caps 
    u'\u201c': '"',             # "“" -> """  double quote LEFT DOUBLE QUOTATION MARK
    u'7': '7',                  # digit
    u'&': u'&',                 # kept Po (73)
    u'%': u'%',                 # kept Po (67)
    u'\u0300': u'\u0300',       # "̀" -> "̀"  kept Mn (58) COMBINING GRAVE ACCENT
    u'[': u'[',                 # kept Ps (34)
    u']': u']',                 # kept Pe (34)
    u'\u2013': u'\u2013',       # "–" -> "–"  kept Pd (33) EN DASH
    u'Q': u'q\xb9',             # decomposed caps 
    u'\u2028': '',              # " " -> ""  dispensible LINE SEPARATOR
    u'\u0302': u'\u0302',       # "̂" -> "̂"  kept Mn (7) COMBINING CIRCUMFLEX ACCENT
    u'+': u'+',                 # kept Sm (6)
    u'Y': u'y\xb9',             # decomposed caps kept letter under threshold 4 < 6
    u'\u201f': '"',             # "‟" -> """  double quote DOUBLE HIGH-REVERSED-9 QUOTATION MARK
    u'\u201e': '"',             # "„" -> """  double quote DOUBLE LOW-9 QUOTATION MARK
    u'\u20ac': '',              # "€" -> ""  removed Sc, 2 < 6 EURO SIGN
    u'\xac': '',                # "¬" -> ""   removed Sm, 1 < 6 NOT SIGN
    u'*': '',                   # removed Po, 1 < 6
    u'\u0327': '',              # "̧" -> ""   removed Mn, 1 < 6 COMBINING CEDILLA
}
# mapping 96 characters to 51, (decomposed)
