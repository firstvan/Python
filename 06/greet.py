#!/bin/python2

def greet(name, greetings="Hello"):
    print '{g} {n}!'.format(g=greetings,n=name)

def main():
    greet('Pyhton')
    greet('Pyhton', greetings="Hola")
    greet('Pyhton', "Bonjour")

if __name__ == "__main__":
    main()
