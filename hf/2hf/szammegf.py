#!/usr/bin/env python2

def megf(szam):
    return int(str(szam)[::-1])

def main():
    i = raw_input("Givemme a number: ")

    print str(megf(int(i)))

if __name__ == "__main__":
    main();
