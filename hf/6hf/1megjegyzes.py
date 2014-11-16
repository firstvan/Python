#!/bin/python2
# encoding: utf-8


def main():
    f = open("string1.py")
    o = open("string1_clean.py", "w")
    i = 0
    for line in f:
        if i== 0 or i == 1:
            o.write(line)

        if line.find("#") == -1 and i!=0 and i != 1:
            o.write(line)
        i +=1

    f.close()
    o.close()


if __name__ == "__main__":
    main()
