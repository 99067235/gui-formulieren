from email import message
from time import strftime
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



# confirm button
def confirm():
    selectedDate = [selectedYear.get(),selectedMonth.get(),selectedDay.get()]
    whatMonth = months.index(f"{selectedMonth.get()}") + 1
    try:
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        d2 = d1.split('/')
        d0 = date(int(d2[2]),int(d2[1]),int(d2[0]))
        d1 = date(int(selectedYear.get()), whatMonth, int(selectedDay.get()))
        delta = d1 - d0
        if delta.days == 0:
            messagebox.showinfo("DATE", f"That is today!")
        else:
            messagebox.showinfo("DATE", f"The epic difference is {delta.days} epic days.")
    except ValueError:
        messagebox.showinfo("AAAAAAAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n That is not right.")
    

# year combobox
selectedYear = tkinter.StringVar()
yearsbox = tkinter.Entry(window,textvariable=selectedYear)
yearsbox.place(x=900, y=25)

# days combobox
selectedDay = tkinter.StringVar()
daysbox = ttk.Combobox(window, text="", values=days, textvariable=selectedDay)
daysbox.place(x=500, y=25)

# months combobox
selectedMonth = tkinter.StringVar()
monthsbox = ttk.Combobox(window, text="", values=months, textvariable=selectedMonth)
monthsbox.place(x=700, y=25)

# confirmbutton
confirmButton = tkinter.Button(window, text="confirm", command=confirm)
confirmButton.place(x=750, y=50)


window.mainloop()