#!/usr/bin/env python
# Prime Factorization - Have the user enter a number and find all Prime Factors
# if there are any) and display them.

def prime_factors(n):

    p_factors = []
    for i in range(2, (n/2)+1):
        if n % i == 0:
            if prime_factors(i) == []:
                p_factors.append(i)
    return p_factors


if __name__ == "__main__":
    number = int(raw_input("Enter the number for which you want prime factors:"))
    print prime_factors(number)
