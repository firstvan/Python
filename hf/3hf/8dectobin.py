#!/usr/bin/env python2

import sys

def decToBin(num):
    li = []
    hanyados = num//2
    li.append(num%2);
    
    while hanyados != 0:
        li.append(hanyados%2);
        hanyados = hanyados//2
    
    for i in li[::-1]:
        sys.stdout.write(str(i))

    print

def main():
    decToBin(156)


if __name__ == "__main__":
    main();
