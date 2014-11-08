#!/bin/python2
# encoding: utf-8

import sys

TEXT=u"""A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""

def ekezet(t):
    """Replace all accentuated letter in TEXT
    """

    ek = {u'á' : 'a', u'é' : 'e', u'í':'i', u'ó':'o', u'ö':'o', u'ő':'o', u'ú':'u', u'ü':'u', u'ű' : 'u', u'Á':'A',u'É':'E',u'Í':'I',u'Ó':'O', u'Ö':'O',u'Ő':'O',u'Ú':'U',u'Ü':'U',u'Ű':'U'}
    k = ek.keys()
    res = []
    for szo in t:
        for c in szo:
            if c in k:
                sys.stdout.write(ek[c])
            else:
                sys.stdout.write(c)
    print

def main():
    ekezet(TEXT)


if __name__ == "__main__":
    main()
