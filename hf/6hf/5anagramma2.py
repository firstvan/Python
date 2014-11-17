#!/bin/python2
# encoding: utf-8

def anagramma(text1, text2):
    li1 = []
    for c in text1:
        li1.append(c)

    li2 = []
    for c in text2:
        li2.append(c)

    li1.sort()
    li2.sort()

    an = True
    if len(li1) == len(li2):
        for c in li1:
            if c not in li2:
                an = False
        if an :
            print "anagramma"

def main():
    anagramma("halap", "alpha")


if __name__ == "__main__":
    main()
