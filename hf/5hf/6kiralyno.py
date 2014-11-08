#!/bin/python2
# encoding: utf-8

def kiralynok(li):
    """Draw the 8 queen chessboard
    
    Queens position in the list. Positions starts with 0 and the from bottom"""
    print "+-----------------+"
    for j in range(len(li)):
        print "|",
        for i in li:
            if i == 7-j:
                print "Q",
            else:
                print ".",

        print "|"

    print "+-----------------+"

def main():
    kiralynok([0,4,7,5,2,6,1,3])
    kiralynok([7,3,0,2,5,1,6,4])


if __name__ == "__main__":
    main()
