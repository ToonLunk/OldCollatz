from collatz import *

# TKINTER/GRAPHICS SECTION

# get user input!


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
