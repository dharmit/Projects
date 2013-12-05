#!/usr/bin/python
# Change Return Program - The user enters a cost and then the amount of money
# given. The program will figure out the change and the number of quarters,
# dimes, nickels, pennies needed for the change.
# Coding this as per Indian currency


def change(cost, payment):
    c = payment - cost
    d = {}
    if c == 0:
        return d

    thousand = c / 1000
    c = c - (thousand * 1000)
    if c == 0:
        d = {1000: thousand}
        return d

    five_hundred = c / 500
    c = c - (five_hundred * 500)
    if c == 0:
        d = {1000: thousand, 500: five_hundred}
        return d

    hundred = c / 100
    c = c - (hundred * 100)
    if c == 0:
        d = {1000: thousand, 500: five_hundred, 100: hundred}
        return d

    fifty = c / 50
    c = c - (fifty * 50)
    if c == 0:
        d = {1000: thousand, 500: five_hundred, 100: hundred, 50: fifty}
        return d

    twenty = c / 20
    c = c - (twenty * 20)
    if c == 0:
        d = {1000: thousand, 500: five_hundred, 100: hundred, 50: fifty,
             20: twenty}
        return d

    ten = c / 10
    c = c - (ten * 10)
    if c == 0:
        d = {1000: thousand, 500: five_hundred, 100: hundred, 50: fifty,
             20: twenty, 10: ten}
        return d

    five = c / 5
    c = c - (five * 5)
    if c == 0:
        d = {1000: thousand, 500: five_hundred, 100: hundred, 50: fifty,
             20: twenty, 10: ten, 5: five}
        return d

    two = c / 2
    c = c - (two * 2)
    d = {1000: thousand, 500: five_hundred, 100: hundred, 50: fifty,
         20: twenty, 10: ten, 5: five, 2: two, 1: c}
    return d

if __name__ == "__main__":
    cost = int(raw_input("Enter the cost price: "))
    payment = int(raw_input("Enter the amount paid: "))

    print "Change to be returned is: "
    pay = change(cost, payment)

    amt = 0
    for i in sorted(pay.iterkeys()):
        if pay[i] != 0:
            print repr(i).rjust(4), ":", repr(pay[i]).rjust(4)
        prod = i * pay[i]
        amt = amt + prod
    print "Final amount is: %f" % amt
