#!/bin/python2
# encoding: utf-8

def charcount(text):
    d = {'whitespace':0, 'other':0, 'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    
    d['whitespace'] = text.count(' ');
    for szo in text.split():
        for c in szo:
            if c in d.keys() :
                d[c] += 1
            else:
                d['other'] += 1

    return d

def main():
    a = charcount("cat and dog !!!") 

    print a

if __name__ == "__main__":
    main()
