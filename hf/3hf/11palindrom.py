#!/usr/bin/env python2
#coding: utf8

def palindrom(s, j):
    if j < len(s)//2:
        j += 1
        if palindrom(s, j) == 1:
            if s[j] == s[len(s) - 1 - j]:
                return 1
            else:
                return 0
    else:
        return 1

def main():
    a = raw_input("Szó: ")
    
    print "Triviális: "
    if a == a[::-1]:
        print "Palindróm"
    else:
        print "Nem palindróm"

    print "Iteratív: "
    for i in range(0,len(a)):
        if a[i] == a[len(a) - 1 - i]:
            bol = 1
        else:
            bol = 0

    if bol == 1:
        print "Palindróm"
    else:
        print "Nem palindróm"


    i = palindrom(a,-1)

    print "Rekurzió: "

    if i == 1:
        print "Palindróm"
    else:
        print "Nem palindróm"

if __name__ == "__main__":
    main();
