#!/bin/python2


def main():
    li = ['auto', 'villamos','metro']
    li = [szo.upper()+'!' for szo in li]
    
    print li

    li = ['aladar', 'bela', 'cecil']
    li = [szo.capitalize() for szo in li]

    print li

    li = [0 for n in xrange(10)]

    print li

    li = [n for n in xrange(1,10+1)]
    li = [2*n for n in li]

    print li

    li = ['1', '2', '3','4','5','6','7','8','9','10']
    li = [int(s) for s in li]

    print li

    s="123456789"
    li = [int(n) for n in s]

    print li

    szoveg = "The quick brown fox jumps over the lazy dog"
    li = [len(n) for n in szoveg.split()]

    print li

    szoveg="python is an awsome language"
    li = [n[0] for n in szoveg.split()]

    print li

    szoveg = "The quick brown fox jumps over the lazy dog"
    li = [(n, len(n)) for n in szoveg.split()]

    print li

    li = [n for n in xrange(10) if n%2==0]

    print li
    
    li = [ n*n for n in xrange(20) if (n*n)%2==0]

    print li

    li = [ n*n for n in xrange(20) if str(n*n)[-1]=='4']

    print li

    li = [chr(n) for n in xrange(ord('A'), ord('Z')+1)]

    print "".join(li)

    li = ['  apple  ', ' banana  ', '     kiwi       ']
    li = [ szo.strip() for szo in li]

    print li

if __name__ == "__main__":
    main()
