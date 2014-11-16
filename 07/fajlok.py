#!/bin/python2
# encoding: utf-8


def main():
    f = open("szoveg.txt", "r")

    #for line in f:
        #line = line.rstrip("\n")
    #tartalom = [sor.rstrip("\n") for sor in f.readlines()]
    tartalom = f.read()
    print "'"+tartalom+"'"
    
    print tartalom

    f.close()

if __name__ == "__main__":
    main()
