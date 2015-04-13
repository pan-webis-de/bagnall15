import es
import en
import gr
import nl
import unicodedata
import re

def nullmapper(x):
    return x

#XXX assumes NFKD norm
def get_charmap(lang):
    if lang is None:
        return nullmapper

    charmap = globals()[lang].charmap

    def mapper(text):
        text = text.decode('utf8')
        text = unicodedata.normalize('NFKD', text)
        return u''.join(charmap.get(x, u'') for x in text).encode('utf8')

    return mapper
