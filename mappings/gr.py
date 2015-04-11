# OPTIONS: threshold 1e-05, dotellipses collapse_latin collapse_digits decompose_caps decompose
decomposed = {
    u' ': u' ',                 # kept Zs (262771)
    u'\u03b1': u'\u03b1',       # "α" -> "α"   GREEK SMALL LETTER ALPHA
    u'\u0301': u'\u0301',       # "́" -> "́"  kept Mn (159677) COMBINING ACUTE ACCENT
    u'\u03bf': u'\u03bf',       # "ο" -> "ο"   GREEK SMALL LETTER OMICRON
    u'\u03b9': u'\u03b9',       # "ι" -> "ι"   GREEK SMALL LETTER IOTA
    u'\u03b5': u'\u03b5',       # "ε" -> "ε"   GREEK SMALL LETTER EPSILON
    u'\u03c4': u'\u03c4',       # "τ" -> "τ"   GREEK SMALL LETTER TAU
    u'\u03bd': u'\u03bd',       # "ν" -> "ν"   GREEK SMALL LETTER NU
    u'\u03c5': u'\u03c5',       # "υ" -> "υ"   GREEK SMALL LETTER UPSILON
    u'\u03b7': u'\u03b7',       # "η" -> "η"   GREEK SMALL LETTER ETA
    u'\u03c1': u'\u03c1',       # "ρ" -> "ρ"   GREEK SMALL LETTER RHO
    u'\u03c3': u'\u03c3',       # "σ" -> "σ"   GREEK SMALL LETTER SIGMA
    u'\u03c0': u'\u03c0',       # "π" -> "π"   GREEK SMALL LETTER PI
    u'\u03ba': u'\u03ba',       # "κ" -> "κ"   GREEK SMALL LETTER KAPPA
    u'\u03bc': u'\u03bc',       # "μ" -> "μ"   GREEK SMALL LETTER MU
    u'\u03c2': u'\u03c2',       # "ς" -> "ς"   GREEK SMALL LETTER FINAL SIGMA
    u'\u03bb': u'\u03bb',       # "λ" -> "λ"   GREEK SMALL LETTER LAMDA
    u'\u03c9': u'\u03c9',       # "ω" -> "ω"   GREEK SMALL LETTER OMEGA
    u'\u03b3': u'\u03b3',       # "γ" -> "γ"   GREEK SMALL LETTER GAMMA
    u'\u03b4': u'\u03b4',       # "δ" -> "δ"   GREEK SMALL LETTER DELTA
    u'.': u'.',                 # kept Po (17155)
    u',': u',',                 # kept Po (16142)
    u'\u03c7': u'\u03c7',       # "χ" -> "χ"   GREEK SMALL LETTER CHI
    u'\u03b8': u'\u03b8',       # "θ" -> "θ"   GREEK SMALL LETTER THETA
    u'\u03c6': u'\u03c6',       # "φ" -> "φ"   GREEK SMALL LETTER PHI
    u'\u03b2': u'\u03b2',       # "β" -> "β"   GREEK SMALL LETTER BETA
    u'\u03b6': u'\u03b6',       # "ζ" -> "ζ"   GREEK SMALL LETTER ZETA
    u'\u03be': u'\u03be',       # "ξ" -> "ξ"   GREEK SMALL LETTER XI
    u'\n': u'\n',               # kept Cc (4239)
    u'\u0395': u'\u03b5\xb9',   # "Ε" -> "ε¹"  decomposed caps  GREEK CAPITAL LETTER EPSILON
    u'\r': '',                  # dispensible
    u'\u0391': u'\u03b1\xb9',   # "Α" -> "α¹"  decomposed caps  GREEK CAPITAL LETTER ALPHA
    u'\u03a4': u'\u03c4\xb9',   # "Τ" -> "τ¹"  decomposed caps  GREEK CAPITAL LETTER TAU
    u'\u03a0': u'\u03c0\xb9',   # "Π" -> "π¹"  decomposed caps  GREEK CAPITAL LETTER PI
    u'\u039a': u'\u03ba\xb9',   # "Κ" -> "κ¹"  decomposed caps  GREEK CAPITAL LETTER KAPPA
    u'\xab': u'\xab',           # "«" -> "«"  kept Pi (2825) LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\xbb': u'\xbb',           # "»" -> "»"  kept Pf (2819) RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\u03a3': u'\u03c3\xb9',   # "Σ" -> "σ¹"  decomposed caps  GREEK CAPITAL LETTER SIGMA
    u'\u039f': u'\u03bf\xb9',   # "Ο" -> "ο¹"  decomposed caps  GREEK CAPITAL LETTER OMICRON
    u'\u039c': u'\u03bc\xb9',   # "Μ" -> "μ¹"  decomposed caps  GREEK CAPITAL LETTER MU
    u'\u03c8': u'\u03c8',       # "ψ" -> "ψ"   GREEK SMALL LETTER PSI
    u'\u0394': u'\u03b4\xb9',   # "Δ" -> "δ¹"  decomposed caps  GREEK CAPITAL LETTER DELTA
    u'0': '7',                  # digit
    u';': u';',                 # kept Po (1752)
    u'e': 's',                  # latin
    u'-': u'-',                 # kept Pd (1385)
    u'\u0393': u'\u03b3\xb9',   # "Γ" -> "γ¹"  decomposed caps  GREEK CAPITAL LETTER GAMMA
    u'\u0397': u'\u03b7\xb9',   # "Η" -> "η¹"  decomposed caps  GREEK CAPITAL LETTER ETA
    u'a': 's',                  # latin
    u'o': 's',                  # latin
    u'i': 's',                  # latin
    u'\u039d': u'\u03bd\xb9',   # "Ν" -> "ν¹"  decomposed caps  GREEK CAPITAL LETTER NU
    u'!': u'!',                 # kept Po (907)
    u'1': '7',                  # digit
    u')': u')',                 # kept Pe (817)
    u'n': 's',                  # latin
    u'r': 's',                  # latin
    u'(': u'(',                 # kept Ps (794)
    u'\u0399': u'\u03b9\xb9',   # "Ι" -> "ι¹"  decomposed caps  GREEK CAPITAL LETTER IOTA
    u'\u0392': u'\u03b2\xb9',   # "Β" -> "β¹"  decomposed caps  GREEK CAPITAL LETTER BETA
    u's': 's',                  # latin
    u'\u0398': u'\u03b8\xb9',   # "Θ" -> "θ¹"  decomposed caps  GREEK CAPITAL LETTER THETA
    u'2': '7',                  # digit
    u'\x85': '',                # "" -> ""   dispensible <unknown>
    u'l': 's',                  # latin
    u't': 's',                  # latin
    u':': u':',                 # kept Po (688)
    u'\u039b': u'\u03bb\xb9',   # "Λ" -> "λ¹"  decomposed caps  GREEK CAPITAL LETTER LAMDA
    u'\u03a7': u'\u03c7\xb9',   # "Χ" -> "χ¹"  decomposed caps  GREEK CAPITAL LETTER CHI
    u'"': '"',                  # double quote
    u'\u03a5': u'\u03c5\xb9',   # "Υ" -> "υ¹"  decomposed caps  GREEK CAPITAL LETTER UPSILON
    u'c': 's',                  # latin
    u'\u0308': u'\u0308',       # "̈" -> "̈"  kept Mn (482) COMBINING DIAERESIS
    u'\u03a1': u'\u03c1\xb9',   # "Ρ" -> "ρ¹"  decomposed caps  GREEK CAPITAL LETTER RHO
    u'\u03a6': u'\u03c6\xb9',   # "Φ" -> "φ¹"  decomposed caps  GREEK CAPITAL LETTER PHI
    u'5': '7',                  # digit
    u'u': 's',                  # latin
    u"'": "'",                  # single quote
    u'3': '7',                  # digit
    u'm': 's',                  # latin
    u'd': 's',                  # latin
    u'p': 's',                  # latin
    u'h': 's',                  # latin
    u'9': '7',                  # digit
    u'`': u'`',                 # kept Sk (356)
    u'g': 's',                  # latin
    u'4': '7',                  # digit
    u'b': 's',                  # latin
    u'f': 's',                  # latin
    u'\u03a9': u'\u03c9\xb9',   # "Ω" -> "ω¹"  decomposed caps  GREEK CAPITAL LETTER OMEGA
    u'6': '7',                  # digit
    u'\u0396': u'\u03b6\xb9',   # "Ζ" -> "ζ¹"  decomposed caps  GREEK CAPITAL LETTER ZETA
    u'S': u's\xb9',             # decomposed caps latin
    u'8': '7',                  # digit
    u'A': u's\xb9',             # decomposed caps latin
    u'7': '7',                  # digit
    u'k': 's',                  # latin
    u'C': u's\xb9',             # decomposed caps latin
    u'v': 's',                  # latin
    u'%': u'%',                 # kept Po (173)
    u'\ufeff': '',              # "﻿" -> ""  dispensible ZERO WIDTH NO-BREAK SPACE
    u'y': 's',                  # latin
    u'B': u's\xb9',             # decomposed caps latin
    u'T': u's\xb9',             # decomposed caps latin
    u'\u039e': u'\u03be\xb9',   # "Ξ" -> "ξ¹"  decomposed caps  GREEK CAPITAL LETTER XI
    u'O': u's\xb9',             # decomposed caps latin
    u'H': u's\xb9',             # decomposed caps latin
    u'M': u's\xb9',             # decomposed caps latin
    u'E': u's\xb9',             # decomposed caps latin
    u'w': 's',                  # latin
    u'F': u's\xb9',             # decomposed caps latin
    u'I': u's\xb9',             # decomposed caps latin
    u'L': u's\xb9',             # decomposed caps latin
    u'D': u's\xb9',             # decomposed caps latin
    u'R': u's\xb9',             # decomposed caps latin
    u'N': u's\xb9',             # decomposed caps latin
    u'P': u's\xb9',             # decomposed caps latin
    u'x': 's',                  # latin
    u'J': u's\xb9',             # decomposed caps latin
    u'G': u's\xb9',             # decomposed caps latin
    u'\t': '  ',                # tab
    u'\u03a8': u'\u03c8\xb9',   # "Ψ" -> "ψ¹"  decomposed caps  GREEK CAPITAL LETTER PSI
    u'/': u'/',                 # kept Po (58)
    u'W': u's\xb9',             # decomposed caps latin
    u'z': 's',                  # latin
    u'V': u's\xb9',             # decomposed caps latin
    u'K': u's\xb9',             # decomposed caps latin
    u'j': 's',                  # latin
    u'@': u'@',                 # kept Po (22)
    u'U': u's\xb9',             # decomposed caps latin
    u'Y': u's\xb9',             # decomposed caps latin
    u'X': u's\xb9',             # decomposed caps kept letter under threshold 16 < 18
    u'&': '',                   # removed Po, 16 < 18
    u'*': '',                   # removed Po, 13 < 18
    u'q': 's',                  # kept letter under threshold 13 < 18
    u'$': '',                   # removed Sc, 6 < 18
    u'?': '',                   # removed Po, 6 < 18
    u'+': '',                   # removed Sm, 4 < 18
    u'Q': u's\xb9',             # decomposed caps kept letter under threshold 4 < 18
    u'<': '',                   # removed Sm, 2 < 18
    u'[': '',                   # removed Ps, 2 < 18
    u'\u2028': '',              # " " -> ""  dispensible LINE SEPARATOR
    u'Z': u's\xb9',             # decomposed caps kept letter under threshold 2 < 18
    u']': '',                   # removed Pe, 2 < 18
}
# mapping 144 characters to 48, (decomposed)
