#!/usr/bin/env python

x = [1]

def fib(n):
    global x
    while len(x) <= n:
        if len(x) == 1:
            x.append(1)
        else:
            x.append(x[-1] + x[-2])

n = int(raw_input("How long Fibonacci series do you want to configure? Enter a number:"))
fib(n)
print x
