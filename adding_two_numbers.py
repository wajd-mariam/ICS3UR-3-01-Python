#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: September 2019
# This program calculates the sum of two number


def main():

    # This program collects two numbers from the user and adds them together
    print("Enter the two numbers you would like to add:")

    # input
    Number1 = input("Enter the first number:")
    Number2 = input("Enter the second number:")

    # process
    add = float(Number1) + float(Number2)

    # output
    print("")
    print("The sum of the two numbers is {}".format(add))


if __name__ == "__main__":
    main()
