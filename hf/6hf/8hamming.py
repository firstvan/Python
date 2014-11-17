#!/bin/python2
# encoding: utf-8

def hamming(text1, text2):
    h = 0
    seged = 0
    
    if len(text1) < len(text2):
        h = len(text2) - len(text1)
        for c in text1:
            if c != text2[seged]:
                h += 1
            seged += 1
    elif len(text2) < len(text1):
        h = len(text1) - len(text2)
        for c in text2:
            if c != text1[seged]:
                h += 1
            seged += 1
    else:
        for c in text1:
            if c != text2[seged]:
                h += 1
            seged += 1


    return h

def main():
    print hamming("toned", "roses")


if __name__ == "__main__":
    main()
