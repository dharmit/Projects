#!/usr/bin/env python

fibonacci = [1]

def fib(n):
    global fibonacci
    while len(fibonacci) <= n:
        if len(fibonacci) == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])

n = int(raw_input("How long Fibonacci series do you want to configure? Enter a number:"))
fib(n)
print fibonacci
