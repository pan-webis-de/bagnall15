
C_NORMAL    = "\033[00m"
DARK_RED    = "\033[00;31m"
RED         = "\033[01;31m"
DARK_GREEN  = "\033[00;32m"
GREEN       = "\033[01;32m"
YELLOW      = "\033[01;33m"
DARK_YELLOW = "\033[00;33m"
DARK_BLUE   = "\033[00;34m"
BLUE        = "\033[01;34m"
PURPLE      = "\033[00;35m"
MAGENTA     = "\033[01;35m"
DARK_CYAN   = "\033[00;36m"
CYAN        = "\033[01;36m"
GREY        = "\033[00;37m"
WHITE       = "\033[01;37m"

REV_RED     = "\033[01;41m"

_FOREGROUND = "\033[38;5;%sm"


def generate_spectrum(starts, step=6, n=6):
    spectrum = []
    for start in starts:
        end = start + step * n
        spectrum.extend(_FOREGROUND % x for x in range(start, end, step))
    return spectrum

spectra = {k: generate_spectrum(x) for k, x
           in (('warm', (160, 196)),
                ('darkwarm', (88, 124)),
                ('bluegreen', (17, 53)),
           )}
