#!/bin/python2

import pygyak

def main():
    n = sum([i for i in xrange(1,200) if pygyak.is_prime(i)])
    
    print n



if __name__ == "__main__":
    main()
