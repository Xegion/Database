from tkinter import *

def check():
    if choice.get() == "search":
        searching = Tk()
        idnum = StringVar()
        idBox = Entry(startWindow, textvariable=idnum, width=10)
        searching.mainloop()
   

startWindow = Tk()
choice = StringVar()
choiceBox = Entry(startWindow, textvariable=choice, width=25)
choiceBox.grid(column=1, row=1)
goButton = Button(startWindow, text="Go", command=check)
goButton.grid(column=1, row=2)
startWindow.mainloop()