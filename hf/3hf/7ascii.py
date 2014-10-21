#!/usr/bin/env python2

def asciiPrint():
    osszeg = 0
    for i in range(32, 127+1):
        print '{s}: {ch}'.format(s=i, ch=chr(i))
        if i >= ord('A') and i <= ord('Z'):
            osszeg += i 

    print 'A-Z char ascii osszege: ' + str(osszeg)

def main():
    asciiPrint()

if __name__ == "__main__":
    main();
