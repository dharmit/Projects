#!/usr/bin/env python

if __name__ == "__main__":
    try:
        n1 = int(raw_input("Number 1: "))
        n2 = int(raw_input("Number 2: "))
    except:
        print "Invalid input"
    else:
        op = raw_input("Operation: '+', '-', '*', '/': ")
        if op in '+-*/':
            print "%d %s %d = %d" % (n1, op, n2, eval(str(n1) + op + str(n2)))
