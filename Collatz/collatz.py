# This program is based on the Collatz Conjecture. Any number you input will eventually lead to the numbers
# 4, 2, then 1. That fact is unproven though - can you find an exception?

# import pretty print module to print the list at the end
import time
from tkinter import *
from pprint import pprint


def showInfo(numList):  # function for displaying information about sequence
    if(len(numList) == 0):
        exit(2)
    else:
        # 1 has to be appended since it's the escape character
        numList.append(1)
        print("\n'*' represents tens, '@' represents hundreds, and '+' shows that the number continues.")

        print("\nSequence (starting with seed): ")
        pprint(numList)  # print out the list
        print("\nTotal nodes in sequence: ", len(numList))
        # to wait (if using in CMD/Terminal/Emulator)
        wait = input("\nPress 'Enter' to continue.")


def getCollatz():
    num = 1  # user input
    stars = 1  # how many stars to print

    while(True):
        # get user input
        numList = []  # list of nodes encountered
        num = int(input("\nEnter '1' to exit, or enter new seed number: "))
        while(num != 1):  # once the sequence hits 1, the closed loop begins
            hundreds = 0
            stars = num / 10  # calculate the number of stars to display

            if num > 100:  # if the number is in the thousands,
                # show a plus symbol for each hundred
                hundreds = (num / 100) + 1
                stars = -1  # show no stars

            print(int(num), end=" ")  # shows the number at base of stars

            tenCount = 0
            for i in range(0, int(stars) + 1):  # for each 10's place in num,
                print("*", end="")            # add a star
                tenCount += 1
                if(tenCount > 100):
                    print("+")

            hunCount = 0  # count how many '@' have been printed
            for i in range(1, int(hundreds)):  # for 100's place
                hunCount += 1
                print("@", end="")  # add an '@'
                if (hunCount > 100):
                    print("+")
                    break

            print()  # for space between rows
            # append the new sequence number to a list
            numList.append(int(num))

            if (num % 2 == 1):  # if the number is odd,
                num = (num * 3) + 1  # multiply by 3, add 1
            else:
                num /= 2  # if the number is even, divide by 2

        showInfo(numList)  # display the information about the sequence


# begin the program
# getCollatz()  # commented out!!!!!!!!!!!!!!!

# the window
screen = Tk()
screen.title("Collatz Conjecture")
screen.geometry("500x500")

# the insides of the window
welcomeText = Label(text="Welcome!",
                    fg="white", bg="#1f1f1f")
welcomeText.pack()

screen.mainloop()
