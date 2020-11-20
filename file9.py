"""
    Author: Hayden Hopkinson
    Date: 20/11/2020
    Description:this file will clear the console so that it does not get overrun by many lines
    code adapted from https://www.geeksforgeeks.org/clear-screen-python/
    version: 1.
    improvements from last version:
"""

# libraries
from os import system, name
# functions


def clear():
    """
    this will wait for the user to make an input of anything before

    """
    input("press enter to continue")
    if name == "nt":
        system("cls")
    else:
        system("clear")


# main

if __name__ == "__main__":
    print("")
