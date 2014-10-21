#!/usr/bin/env python2

def osszeg():
    sum1 = 0
    for i in range(1,100+1):
        sum1 += i;

    print sum1

def szamjegyosszeg():
    li = []
    for i in range(1,100+1):
        li += str(i);
        

    sum2 = 0
    for s in li:
        sum2 += int(s)

    return sum2

def main():
    osszeg()
    print szamjegyosszeg()


if __name__ == "__main__":
    main();
