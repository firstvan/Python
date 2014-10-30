#!/bin/python2
# encoding: utf-8



def diamond(a):
    if a % 2 != 1:
        print "Nem páratlan a szám"
        return -1

    li = []
    
    for i in xrange(0,(a+1)/2):
        li.append('*')
        for j in xrange(0, i):
            li[i] += '**'
    
    for i in xrange((a+1)/2, a):
        li.append('*')
        for j in xrange (i+2, a+1):
            li[i] += '**'

    for i in li:
        print i.center(a)



def main():
    diamond(7)


if __name__ == "__main__":
    main()
