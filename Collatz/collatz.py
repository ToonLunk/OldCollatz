# This program is based on the Collatz Conjecture. Any number you input will eventually lead to the numbers
# 4, 2, then 1. That fact is unproven though - can you find an exception?


import time
# import tkinter for graphics
from tkinter import *
# import pretty print module to print the list at the end
from pprint import pprint


def wait():  # use wait() to wait 1 second
    time.sleep(1)

# legacy


def showInfo(numList):  # function for displaying information about sequence
    if(len(numList) == 0):
        exit(2)
    else:
        # 1 has to be appended since it's the escape character
        print("\n'*' represents tens, '@' represents hundreds, and '+' shows that the number continues.")

        print("\nSequence (starting with seed): ")
        pprint(numList)  # print out the list
        print("\nTotal nodes in sequence: ", len(numList))
        # to wait (if using in CMD/Terminal/Emulator)
        wait = input("\nPress 'Enter' to continue.")


def getCollatz(num):
    while(True):
        # get user input
        numList = []  # list of nodes encountered
        while(True):  # once the sequence hits 1, the closed loop begins

            numList.append(int(num))

            # return list if it hits 1
            if (num == 1):
                return numList

            if (num % 2 == 1):  # if the number is odd,
                num = (num * 3) + 1  # multiply by 3, add 1
            else:
                num /= 2  # if the number is even, divide by 2
