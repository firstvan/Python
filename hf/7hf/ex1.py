#!/bin/python2
# encoding: utf-8

import pygyak

def main():
    li = [i for i in xrange(1,100) if pygyak.is_prime(i)]
    
    print li



if __name__ == "__main__":
    main()
