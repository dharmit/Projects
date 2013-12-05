#!/usr/bin/env python


def mortgage_calculator(months, amount, interest):
    final_amount = amount + ((amount * interest)/100)
    return int(final_amount / months)

if __name__ == "__main__":
    amt = int(raw_input("Enter the amount: "))
    interest = int(raw_input("Enter the interest rate: "))
    months = int(raw_input("Enter the number of months: "))
    print "Mortgage to be paid per month is: %d" % mortgage_calculator
    (months, amt, interest)
