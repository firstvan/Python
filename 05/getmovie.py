#!/bin/python2


def get_movie_info():
    return ['Total Recall', 1990, 7.5]


def main():
    cim, ev, pontszam = get_movie_info()
    print "Cim:", cim
    print "Ev:", ev
    print "Pontszam:", pontszam

if __name__ == "__main__":
    main()
