import es
import en
import gr
import nl
import unicodedata

def nullmapper(x):
    return x


#XXX assumes NFKD norm
def get_charmap(lang):
    if lang is None:
        return nullmapper

    charmap = globals()[lang].charmap
    m = charmap.__getitem__

    def mapper(text):
        text = text.decode('utf8')
        text = unicodedata.normalize('NFKD', text)
        return ''.join(m(x) for x in text).encode('utf8')

    return mapper
