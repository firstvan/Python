#!/bin/python2

def ciklus(num, debug=False):
    if debug:
        print '#start: loop'
    for n in xrange(num+1):
        print n,

    print
    if debug:
        print '#end: loop'

def main():
    ciklus(9)
    ciklus(9, True)

if __name__ == "__main__":
    main()
