#!/bin/python2
# encoding: utf-8


def main():
    f = open("szamok")

    osszeg = 0

    for line in f:
        osszeg += int(line)

    print str(osszeg)[:10]


if __name__ == "__main__":
    main()
