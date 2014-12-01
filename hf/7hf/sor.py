#!/bin/python2
# encoding: utf-8

class Sor(object):
    def __init__(self):
        self.li1 = []
        self.li2 = []

    def append(self, v):
        if len(self.li1) == 0 and len(self.li2) == 0:
            self.li1.append(v)
        elif len(self.li1) == 0 and len(self.li2) != 0:
            self.li1.append(v)
            for i in xrange(len(self.li2)):
                self.li1.append(self.li2.pop())
        elif len(self.li1) != 0 and len(self.li2) == 0:
            self.li2.append(v)
            for i in xrange(len(self.li1)):
                self.li2.append(self.li1.pop())
 
    def popleft(self):
        if len(self.li1) != 0:
            return self.li1.pop()
        else:
            return self.li2.pop()

    def __str__(self):
        if len(self.li1) != 0:
            return str(self.li1[::-1])
        else:
            return str(self.li2[::-1])

    def is_empty(self):
        return len(self.li1) == 0 and len(self.li2) == 0
    
    def size(self):
        if len(self.li1) != 0:
            return len(self.li1)
        else:
            return len(self.li2)

def main():
    s = Sor()
    print s.is_empty()
    s.append(4)
    print s.is_empty()
    print s.size()
    x = s.kivesz()

if __name__ == "__main__":
    main()
