#!/bin/python2


def main():
    ossz=0;
    ossz1=0;
    for i in xrange(1,100+1):
        ossz += i**2
        ossz1 += i

    print (ossz1**2) - ossz

if __name__ == "__main__":
    main()
