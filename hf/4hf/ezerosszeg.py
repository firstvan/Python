#!/bin/python2

def main():

    print sum([n for n in xrange(0, 1000) if n%3==0 or n%5==0])

if __name__ == "__main__":
    main()
