# -*- coding: utf-8 -*-
# OPTIONS: threshold 1e-05, dotellipses collapse_dashes collapse_digits decompose_caps decompose
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
    u'I': u'i\xb9',             # decomposed caps 
    u'v': u'v',
    u'!': u'!',                 # kept Po (1901)
    u'A': u'a\xb9',             # decomposed caps 
    u'?': u'?',                 # kept Po (1336)
    u'T': u't\xb9',             # decomposed caps 
    u'W': u'w\xb9',             # decomposed caps 
    u'S': u's\xb9',             # decomposed caps 
    u'H': u'h\xb9',             # decomposed caps 
    u'M': u'm\xb9',             # decomposed caps 
    u'Y': u'y\xb9',             # decomposed caps 
    u'B': u'b\xb9',             # decomposed caps 
    u'O': u'o\xb9',             # decomposed caps 
    u'C': u'c\xb9',             # decomposed caps 
    u'D': u'd\xb9',             # decomposed caps 
    u'N': u'n\xb9',             # decomposed caps 
    u'G': u'g\xb9',             # decomposed caps 
    u';': u';',                 # kept Po (313)
    u'L': u'l\xb9',             # decomposed caps 
    u'j': u'j',
    u'P': u'p\xb9',             # decomposed caps 
    u'F': u'f\xb9',             # decomposed caps 
    u'q': u'q',
    u'E': u'e\xb9',             # decomposed caps 
    u'\t': '  ',                # tab
    u'x': u'x',
    u'R': u'r\xb9',             # decomposed caps 
    u'"': '"',                  # double quote
    u'J': u'j\xb9',             # decomposed caps 
    u'z': u'z',
    u'V': u'v\xb9',             # decomposed caps 
    u'K': u'k\xb9',             # decomposed caps 
    u'Q': u'q\xb9',             # decomposed caps 
    u'U': u'u\xb9',             # decomposed caps 
    u'_': u'_',                 # kept Pc (42)
    u':': u':',                 # kept Po (40)
    u'[': u'[',                 # kept Ps (24)
    u'(': u'(',                 # kept Ps (23)
    u')': u')',                 # kept Pe (21)
    u']': u']',                 # kept Pe (15)
    u'}': u'}',                 # kept Pe (10)
    u'{': u'{',                 # kept Ps (7)
    u'\\': u'\\',               # kept Po (3)
    u'\u0300': '',              # "̀" -> ""   removed Mn, 2 < 3 COMBINING GRAVE ACCENT
    u'Z': u'z\xb9',             # decomposed caps kept letter under threshold 2 < 3
}
# mapping 72 characters to 46, (decomposed)
