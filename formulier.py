from tkinter import ttk
import tkinter as tk
import tkinter
from tkinter import ttk

window = tk.Tk()
window.geometry("1920x1080")
window.title("Minecraft Registration form")
nameLabel = tkinter.Label(window, text="What's your name?", font=('Helvatical bold',15)).pack()
yourName = tkinter.StringVar(value = "")
name = tkinter.Entry(window, textvariable=yourName, width=50, font=50).pack()

hoursLabel = tkinter.Label(window, text="How many hours have you played Minecraft?", font=('Helvatical bold',15)).pack()
yourHours = ttk.Spinbox(window, from_=0, to=float("inf"), width=50, font=50).pack()

var = tkinter.IntVar()
friendsLabel = tkinter.Label(window, text="Do you want to play with other people?", font=('Helvatical bold',15)).pack()
rButton1 = tkinter.Radiobutton(window, text="Yes", variable=var, value=1, width=50, font=50).pack()
rButton2 = tkinter.Radiobutton(window, text="No", variable=var, value=2, width=50, font=50).pack()

emailLabel = tkinter.Label(window, text="Enter your email below", font=('Helvatical bold',15), anchor="center").pack()
emailVar = tkinter.StringVar()
emailEntry = tkinter.Entry(window, textvariable=emailVar, width=50, font=50).pack()
window.mainloop()