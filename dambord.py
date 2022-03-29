import tkinter as tk
from tkinter import *
import tkinter

window = tk.Tk()
window.title("dambord")

def dambord():
    i = 0
    columnNumber = 0
    rowNumber = 0
    for l in range(10):
        columnNumber += 1
        for i in range(10):
            if (l % 2) == 0:
                if (i % 2) == 0:
                    blacklabel = tk.Label(window,bg="black", height=1, width=2)
                    blacklabel.grid(column=i, row=rowNumber)
                else:
                    whitelabel = tk.Label(window,bg="white", height=1, width=2)
                    whitelabel.grid(column=i, row=rowNumber)
            else:
                if (i % 2) == 0:
                    whitelabel = tk.Label(window,bg="white", height=1, width=2)
                    whitelabel.grid(column=i, row=rowNumber)
                else:
                    blacklabel = tk.Label(window,bg="black", height=1, width=2)
                    blacklabel.grid(column=i, row=rowNumber)
        rowNumber += 1
dambord()

window.mainloop()