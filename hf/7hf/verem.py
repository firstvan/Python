#!/bin/python2
# encoding: utf-8


class Verem(object):
    def __init__(self):
        self.li = []
    
    def betesz(self, a):
        self.li.append(a)

    def kivesz(self):
        if self.ures():
            return None
        else:
            return self.li.pop()

    def __str__(self):
        s = "[ "
        for i in self.li:
            s +=str(i)+" "

        return s

    def ures(self):
        return len(self.li) == 0

    def meret(self):
        return len(self.li)

def main():
    v = Verem()
    print v
    print v.ures()    
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print v
    print v.meret() # 3
    print v.ures()  # False
    x = v.kivesz()
    print x         # 5
    print v         # [1 4
    v.kivesz()
    v.kivesz()      # most már üres
    x = v.kivesz()
    print x

if __name__ == "__main__":
    main()
