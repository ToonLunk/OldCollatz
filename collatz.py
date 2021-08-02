# import pretty print module to print the list at the end
from pprint import pprint 

num = 1
numList = []
numStars = 1

while(num != 0): # if the user enters "0", end the program
    num = int(input("Enter the seed number: ")) # get user input
    while(num != 4): # once the sequence hits 4, the closed loop begins
        numStars = num / 10 # calculate the number of stars to display
        print(int(num), end=" ") # shows the number at base of stars
        
        for i in range(0, int(numStars) +1): # for each 10's place in num, 
            print("*",end="")            # add a star
        print("@") # for whitespace after stars
        numList.append(int(num)) # append the new sequence number to a list
        
        if (num % 2 == 1): # if the number is odd, 
            num = (num * 3) + 1 # multiply by 3, add 1
        else:
            num /= 2 # if the number is even, divide by 2
        
    pprint(numList)
    wait = input() # to wait (if using in CMD/Terminal/Emulator)