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

# TKINTER/GRAPHICS SECTION


# get user input


def addButton(number, symbol, buttonColor, curFrame):
    Button(curFrame, text=(str(number) + str(symbol)),
           bg=buttonColor, width=25, pady=1, borderwidth=0).pack()


def submitButton():
    temp = 0  # temporary number to check size of last

    num = prompt.get()
    num = int(num)
    numList = getCollatz(num)
    frame = main_frame

    for i in range(0, len(numList)):
        if(numList[i] > temp):
            addButton(numList[i], " (+)", "green", frame)
        else:
            addButton(numList[i], " (-)", "red", frame)
        temp = numList[i]


screen = Tk()  # create the "screen"
screen.title("Collatz Project -Toon Lunk")  # titlebar for the screen
screen.geometry("480x480")  # size of the screen

prompt = Entry(screen, width=20)
prompt.focus_set()
prompt.pack()

Button(screen, text="Submit", command=submitButton).pack()

main_frame = Frame(screen)
main_frame.pack()

screen.mainloop()
