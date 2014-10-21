#!/usr/bin/env python2

import sys

szoveg ='''
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

    Aqmimjjyi:

        Ynyb'''

def main():
    for ch in szoveg:
        if ch == 'k':
            sys.stdout.write('m')
        elif ch == 'o':
            sys.stdout.write('q')
        elif ch == 'e':
            sys.stdout.write('g')
        else:
            sys.stdout.write(ch)

    print

if __name__ == "__main__":
    main();
