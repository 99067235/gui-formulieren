from email import message
import tkinter as tk
from tkinter import *
import tkinter
from tkinter import ttk
from datetime import date  
import datetime
from tkinter import messagebox 
window = tk.Tk()
window.geometry("1920x1080")
days = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
dateLabel = tk.Label(window, text="Date:").pack()

# check date
dateCheck = datetime.datetime.now()
currentDay = dateCheck.strftime("%d")
currentMonth = dateCheck.strftime("%m")
Year = dateCheck.strftime("%y")
currentYear = str(20) + Year
currentDate = int(currentDay), int(currentMonth), int(currentYear)
print(currentDate)


# confirm button
def confirm():
    daysInput = daysbox.get()
    monthInput = monthsbox.get()
    index = months.index(monthInput)
    yearInput = yearsbox.get()
    inputDate = int(daysInput), index + 1, int(yearInput)
    print(inputDate)
    if yearInput == "amogus":
        messagebox.showinfo("amogus", "sus")
    elif yearInput == "69":
        messagebox.showerror("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    elif inputDate == currentDate:
        messagebox.showerror("", "ITS A EPIC DAY!")
    window.destroy()

# year combobox
year = tkinter.StringVar(value=currentYear)
yearsbox = tkinter.Entry(window,textvariable=year)
yearsbox.place(x=900, y=25)

# days combobox
daysbox = ttk.Combobox(window, textvariable= currentDay, values=days)
daysbox.place(x=500, y=25)

# months combobox
monthsbox = ttk.Combobox(window, textvariable=currentMonth, values=months)
monthsbox.place(x=700, y=25)

# confirmbutton
confirmButton = tkinter.Button(window, text="confirm", command=confirm)
confirmButton.place(x=750, y=50)


window.mainloop()










































































































