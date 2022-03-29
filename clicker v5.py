from email import message
from itertools import tee
import tkinter as tk
from tkinter import *
import tkinter
from tkinter import messagebox
import time
import threading

window = tk.Tk()
window.configure(bg="grey")
window.geometry("500x500")
window.title("clicker")

window.counter = 0
amountUp = 0
amountDown = 0
mycounter = window.counter
lastButton = "button"
def color():
    if window.counter == 0:
        window.configure(bg= "grey")
    elif window.counter < 0:
        window.configure(bg= "red")
    else:
        window.configure(bg="green")

def HoverColor(event):
    if window.counter == 0:
        window.configure(bg= "grey")
    elif window.counter < 0:
        window.configure(bg= "red")
    else:
        window.configure(bg="green")

### optellen
def up():
    global lastButton, amountUp
    checkBoxButton.configure(state= NORMAL)
    amountUp += 1
    lastButton = "up"
    window.counter += 1
    color()
    Mylabel['text'] = str(window.counter)

def changeColor(event):
    window.configure(bg= "yellow")

### aftellen
def down():
    global lastButton, amountDown
    checkBoxButton.configure(state= NORMAL)
    amountDown += 1 
    lastButton = "down"
    window.counter -= 1
    color()
    Mylabel['text'] = str(window.counter)

def labelClick(event):
    if lastButton == "up":
        amount = amountUp * 3
        Mylabel['text'] = str(amount)
    else:
        amount = amountDown / 3
        Mylabel["text"] = str(amount)

def autoClicker():
    while True:
        time.sleep(0.5)
        if AutoEnabled.get() == True:
            if lastButton == "up":
                up()
            elif lastButton == "down":
                down()

### button optellen
buttonUP = Button(window, text="Up", height=2, width=30, command=up)
window.bind("=", up)
window.bind("<Up>", lambda event: up())
buttonUP.pack()

### label getal
Mylabel = Label(window, text="0", height=2, width=30)
Mylabel.bind("<Double-Button-1>", labelClick)
window.bind("<space>", labelClick)
Mylabel.pack()

### button aftellen
buttonDown = Button(window, text="Down", height=2, width=30, command=down)
window.bind("-", down)
window.bind("<Down>", lambda event: down())
buttonDown.pack()

checkBoxState = False
AutoEnabled = tkinter.BooleanVar()
checkBoxButton = tkinter.Checkbutton(variable=AutoEnabled,text="AutoClicker",state=tkinter.DISABLED)
checkBoxButton.place(x=0, y=30)
threading.Timer(1,autoClicker).start()
window.mainloop()