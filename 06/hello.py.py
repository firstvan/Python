#!/bin/python2

def hello(name, repeat= 1, postfix=""):
    for i in xrange(repeat):
        print name, postfix

def main():
    hello('Lac', 3)
    hello('Py')
    hello('Guido', 2, '?')
    hello('Guido', postfix='!', repeat=2)
    hello('Guido', postfix='!')


if __name__ == "__main__":
    main()
