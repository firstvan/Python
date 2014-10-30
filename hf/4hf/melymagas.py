#!/bin/python2
# encoding: utf-8

MAGAS = ['e', u'é', 'i', u'í', u'ö', u'ő', u'ü', u'ű']
MELY = ['a', u'á', 'o', u'ó', 'u', u'ú']

words = ["ablak", u"erkély", u"kisvasút", "magas", u"mély"]

def main():
    for szo in words:
        mely=magas=0;
        for c in szo:
            if c in MAGAS:
                magas +=1
            elif c in MELY:
                mely +=1
        
        if mely > 0 and magas > 0:
            print szo + " -> vegyes"
        elif mely > 0:
            print szo + " -> mély"
        elif magas > 0:
            print szo + " -> magas"


if __name__ == "__main__":
    main()
