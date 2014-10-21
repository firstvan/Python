#!/usr/bin/env python2



def main():
    osszeg = 0
    for i in range(0,1000):
        if i % 3 == 0 or i % 5 ==0:
            osszeg += i

    print osszeg


if __name__ == "__main__":
    main();
