#!/usr/bin/env python


def cost(cost, width, height):
    return cost * width * height

if __name__ == "__main__":
    c = int(raw_input("Enter the cost: "))
    w = int(raw_input("Enter the width: "))
    h = int(raw_input("Enter the height: "))
    print cost(c, w, h)
