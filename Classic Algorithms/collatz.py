#/usr/bin/env python

# Collatz Conjecture - Start with a number n > 1. Find the number of steps it
# takes to reach one using the following process: If n is even, divide it by
# 2. If n is odd, multiply it by 3 and add 1.

def collatz(start):
    steps = 0
    number = start

    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = (number * 3) + 1
        steps += 1
    return steps

if __name__ == "__main__":
    start = int(raw_input("Enter the number to start from: "))
    print collatz(start)
