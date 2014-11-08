#!/bin/python2
# encoding: utf-8


def main():
    """Remove duplicated elem from a list
    """
    li = [5, 2, 3, 5, 1, 4, 5, 1, 3, 2, 2, 5]
    res = list(set(li))
    res.sort()
    print res;


if __name__ == "__main__":
    main()
