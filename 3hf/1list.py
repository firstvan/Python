#!/usr/bin/env python2

def lszorzat(lista):

    szor = 1

    for i in lista:
        szor *= i;

    return szor


def main():

    li = [1,2,3,4,5,6]
    
    print lszorzat(li)


if __name__ == "__main__":
    main();
