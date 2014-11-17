#!/bin/python2
# encoding: utf-8

def anagramma(text1, text2):
    
    li = []

    for c in text1:
        if c not in li:
            li.append(c)

    d1 = {}
    for c in li:
        d1[c] = 0

    for c in d1.keys():
        d1[c] = text1.count(c)

    li = []
    for c in text2:
        if c not in li:
            li.append(c)
    
    
    d2 = {}
    for c in li:
        d2[c] = 0

    for c in d2.keys():
        d2[c] = text2.count(c)
    e = True
    li1 = d1.keys()
    li2 = d2.keys()
    
    for c in li1:
        if c not in li2:
            e = False

    for c in li2:
        if c not in li1:
            e = False
    
    li1 = d1.values()
    li2 = d2.values()

    if li1 != li2:
        e = False

    if e:
        print "anagramma"

def main():
    anagramma("aapha", "haapa")


if __name__ == "__main__":
    main()
