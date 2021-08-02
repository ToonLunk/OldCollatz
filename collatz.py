# This program is based on the Collatz Conjecture. Any number you input will eventually lead to the numbers
# 4, 2, then 1. That fact is unproven though - can you find an exception?

# import pretty print module to print the list at the end
from pprint import pprint 

def showInfo(numList): # function for displaying information about sequence
    if(len(numList) < 0):
        exit(2)
    else:
        print(len(numList))
        print("\nSequence (starting with seed): ")
        pprint(numList) # print out the list
        print("\nTotal nodes in sequence: ", len(numList))
        wait = input("\nPress 'Enter' to continue.") # to wait (if using in CMD/Terminal/Emulator)

num = 1
numList = [] # list of nodes encountered
stars = 1 # how many stars to print

while(True): 
    num = int(input("\nEnter '4' to exit, or enter new seed number: ")) # get user input
    while(num != 4): # once the sequence hits 4, the closed loop begins
        stars = num / 10 # calculate the number of stars to display
        print(int(num), end=" ") # shows the number at base of stars
        
        for i in range(0, int(stars) +1): # for each 10's place in num, 
            print("*",end="")            # add a star
        print("@") # for whitespace after stars
        numList.append(int(num)) # append the new sequence number to a list
        
        if (num % 2 == 1): # if the number is odd, 
            num = (num * 3) + 1 # multiply by 3, add 1
        else:
            num /= 2 # if the number is even, divide by 2
       
    showInfo(numList)