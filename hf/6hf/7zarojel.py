#!/bin/python2
# encoding: utf-8

def test(text):
    k = 0; 
    sz = 0;
    kap = 0;
    tempk = 0;
    for c in text:
        #kerek zárójelek vizsgálata
        if c == "(":
            k += 1
        if c == ")":
            k -= 1
        if k < 0:
            print "helytelen zárójelezés"
            break
    
        #szögletes zárójelek vizsgálata
        if c == "[":
            sz += 1
        if c == "]":
            sz -= 1
        if sz < 0:
            print "helytelen zárójelezés"
            break

        #kapcsos zárójelek vizsgálata
        if c == "{":
            kap += 1
        if c == "}":
            kap -= 1
        if kap < 0:
            print "helytelen zárójelezés"
            break
       
        if c == "]" and k != 0:
            print "helytelen zárójelezés"
            break

        if c == "}" and k != 0 and sz != 0:
            print "helytelen zárójelezés"
            break

    if k == 0 and sz == 0 and kap == 0:
        print "Helyes"

def main():
    test("{[()()()[]()()]}")


if __name__ == "__main__":
    main()
