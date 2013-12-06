#!/usr/bin/env python


def decimal_to_binary(n):
    binary = []
    while n != 0:
        binary.append(str(n % 2))
        n = n/2
    binary.reverse()
    return ''.join(binary)


def binary_to_decimal(n):
    decimal = 0
    count = 0
    rev = ''

    for i in range(1, len(n)+1):
        rev += n[-i]

    for i in rev:
        decimal = decimal + (int(i) * (2 ** count))
        count += 1
    return decimal

if __name__ == "__main__":
    print "1. Decimal to Binary"
    print "2. Binary to Decimal"
    choice = int(raw_input("Enter your choice: "))

    if choice == 1:
        decimal = int(raw_input("Enter the decimal to be converted to binary: "
                                ))
        print
        print "Binary of %d is: %s" % (decimal, decimal_to_binary(decimal))
    elif choice == 2:
        binary = raw_input("Enter the binary to be converted to decimal: ")
        print
        print "Decimal of %s is: %d" % (binary, binary_to_decimal(binary))
    else:
        print "You made an invalid choice"
