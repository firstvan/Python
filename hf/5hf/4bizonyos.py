#!/bin/python2
# encoding: utf-8

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """Return characters from text, which in chars
    
    """
    li = []

    for c in text:
        if c in chars:
            li.append(c);

    return "".join(li)

def main():
    print valid("Breaking!")
    print valid("KL754", "0123456789")
    print valid("BEAN", "")

if __name__ == "__main__":
    main()
