#!/usr/bin/env python2
#coding: utf8
import sys

def main():
    
    if len(sys.argv) != 3:
        sys.stderr.write("Kevés argumentum")
        sys.exit(-1)

    szam = float(sys.argv[1]) + float(sys.argv[2])
    print str(szam)

    a = raw_input("first: ")
    b = raw_input("second: ")
    szam = int(a) + int(b)
    print str(szam)

if __name__ == "__main__":
    main();
