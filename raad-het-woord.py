from email import message
import tkinter
import tkinter as tk
from tkinter import messagebox

def confirmButton():
    wordEntryCheck = wordEntry.get()
    if wordEntryCheck.isnumeric():
        messagebox.showerror("Error", "please don't use numbers")
    else:
        daEpicWindow.destroy()
        gameWindow = tk.Tk()
        gameWindow.geometry("1920x1080")
    

daEpicWindow = tk.Tk()
daEpicWindow.geometry("1920x1080")
daEpicWindow.title("configuration window")
infoLabel1 = tkinter.Label(daEpicWindow, text="Type a word")
infoLabel1.place(relx=.5, rely=0.01, anchor="center")

wordVar = tkinter.StringVar(value="")
wordEntry = tkinter.Entry(daEpicWindow, textvariable=wordVar)
wordEntry.place(relx=.5, rely=0.05, anchor="center")
infoLabel2 = tkinter.Label(daEpicWindow, text="4 - 7 characters").place(relx=.5, rely=0.08, anchor="center")
startButton = tkinter.Button(daEpicWindow, text="confirm",command=confirmButton).place(relx=.5, rely=0.12, anchor="center")
daEpicWindow.mainloop()