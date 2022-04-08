from email import message
import random
from socket import getnameinfo
from tkinter import messagebox, ttk
import tkinter as tk
import tkinter, re
from tkinter import ttk
from tkinter.font import Font
import webbrowser
fontSize = 15
mailCharacters = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def error(info):
    messagebox.showinfo("ERROR", info)

def playFriends(want):
    friendsLabel2 = tk.Label(overviewWindow, text=f"{want} to play games with friends\n", font=('Helvatical bold',fontSize)).pack()

def overview():
    global overviewWindow
    window.destroy()
    overviewWindow = tk.Tk()
    overviewWindow.geometry("1920x1080")
    nameView = tk.Label(overviewWindow, text=f"Name:\n{yourName.get()}\n", font=('Helvatical bold',fontSize)).pack()
    hoursView = tk.Label(overviewWindow, text=f"Playtime in Minecraft:\n{hoursVar.get()} hours.\n", font=('Helvatical bold',fontSize)).pack()
    ageView = tk.Label(overviewWindow, text=f"Age: {yourage.get()}\n", font=('Helvatical bold',fontSize)).pack()
    if var.get() == 1:
        playFriends("Wants")
    elif var.get() == 2:
        playFriends("Don't wants")
    else:
        messagebox.showinfo("Error", "Please choose a option (question 3)")
    emailView = tk.Label(overviewWindow, text=f"Email:\n{emailVar.get()}\n", font=('Helvatical bold',fontSize)).pack()
    if specialVar.get() != "":
        specialView = tk.Label(overviewWindow, text=f"You think this is epic about you:\n {specialVar.get()}", font=('Helvatical bold',fontSize)).pack()
    epicRegistrationCode = random.randint(99999,1000000)
    registrationLabel = tk.Label(overviewWindow, text=f"Your epic-unique registration code:\n {epicRegistrationCode}", font=('Helvatical bold',fontSize)).pack()
    overviewWindow.mainloop()

def check(email):
    if yourage.get() <=3:
        messagebox.showinfo("Too young", "You're too young for this event")
    elif hoursVar.get() <= 100:
        messagebox.showinfo("Hours", "You need to have at least 100 hours playtime")
    elif(re.search(mailCharacters,email)):
        overview()
    else:
        messagebox.showinfo("Email error", "Please enter a valid email")

def confirm():
    if yourName.get().isalpha():
        check(emailVar.get())
    if yourName.get() == "":
        error("Please enter your name")
    else:
        pass

window = tk.Tk()
window.geometry("1920x1080")
window.title("Minecraft Registration form")
titleLabel = tkinter.Label(window, text="Minecraft registration form\n", font=('Helvatical bold',fontSize)).pack()
nameLabel = tkinter.Label(window, text="1. What's your name?", font=('Helvatical bold',fontSize)).pack()
yourName = tkinter.StringVar(value = "")
name = tkinter.Entry(window, textvariable=yourName, width=30, font=50)
name.focus()
name.pack()

ageLabel = tkinter.Label(window, text="2. What's your age?", font=('Helvatical bold',fontSize)).pack()
yourage = tkinter.IntVar(value = 0)
age = ttk.Spinbox(window, from_=0, to=100,textvariable=yourage, width=40).pack()

hoursVar = tk.IntVar()
hoursLabel = tkinter.Label(window, text="3. How many hours have you played Minecraft?", font=('Helvatical bold',fontSize)).pack()
yourHours = ttk.Spinbox(window, from_=0, to=float("inf"), textvariable=hoursVar, width=40).pack()

var = tkinter.IntVar()
friendsLabel = tkinter.Label(window, text="4. Do you want to play with other people?", font=('Helvatical bold',fontSize)).pack()
rButton1 = tkinter.Radiobutton(window, text="Yes", variable=var, value=1, width=50, font=50).pack()
rButton2 = tkinter.Radiobutton(window, text="No", variable=var, value=2, width=50, font=50).pack()

emailLabel = tkinter.Label(window, text="5. Enter your email below", font=('Helvatical bold',fontSize), anchor="center").pack()
emailVar = tkinter.StringVar()
emailEntry = tkinter.Entry(window, textvariable=emailVar, width=30, font=50).pack()

specialLabel = tkinter.Label(window, text="Do you want to say something epic about yourself?\n (If not, don't fill in anything)", font=('Helvatical bold',fontSize)).pack()
specialVar = tkinter.StringVar()
specialEntry = tkinter.Entry(window, textvariable=specialVar, width=30, font=50).pack()
confirmButton = tkinter.Button(window, text="Confirm", command=confirm).pack()
window.mainloop()