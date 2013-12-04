#!/usr/bin/env python
import math
n = 2


def get_prime():
    global n
    isPrime = True

    if n == 2:
        n += 1
        return 2
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                isPrime = False
                break
        if isPrime:
            prime = n
            n += 1
            return prime
        else:
            n += 1
            return get_prime()


if __name__ == "__main__":
    next = 'y'
    while next != 'n':
        next = raw_input("Enter 'n' to stop generating prime numbers: ")
        prime = get_prime()
        if prime:
            print prime
