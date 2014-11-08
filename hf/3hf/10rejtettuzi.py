#!/usr/bin/env python2

import sys

szoveg ='''Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb'''

def main():
    szoveg1=''

    for ch in szoveg:
        a = chr(ord(ch) + 2)
        if a == '{':
            szoveg1 += 'a'
        elif a =='[':
            szoveg1 += 'A'
        elif a =='<':
            szoveg1 += ':'
        elif ch =='!' or ch == ' ' or ch == '\n':
            szoveg1 += ch
        else:
            szoveg1 += a


    print szoveg1

if __name__ == "__main__":
    main();
