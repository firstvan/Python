#!/bin/python2

import sys
import random as r

UPTO = 100

def main():
    for i in xrange(UPTO):
        sys.stdout.write(str(r.randint(0, 9)))
        if i != 0 and (i+1) % 10==0: 
            print

if __name__ == "__main__":
    main()
