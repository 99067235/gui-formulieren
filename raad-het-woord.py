from email import message
import string
import tkinter
import tkinter as tk
from tkinter import END, messagebox
from tkinter.messagebox import askretrycancel
Letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def destroyWindow():
    retryWindow.destroy()

def commandCheckButton(): # checks the given letters
    global retryWindow
    answer = []
    answer.append(var1.get())
    answer.append(var2.get())
    answer.append(var3.get())
    answer.append(var4.get())
    answer.append(var5.get())
    answer.append(var6.get())
    answer.append(var7.get())
    while '' in answer:
        answer.remove('')
    if answer == wordlist:
        messagebox.showinfo("Congrats!", "You guessed the word! Your score is")
    else:
        gameWindow.destroy()
        retryWindow = tk.Tk()
        retryWindow.title("Retry?")
        retryWindow.geometry("500x200")
        retryLabel = tk.Label(retryWindow, text="You didn't guess the word, try again", font=('Helvatical bold',15)).place(x=100, y=50)
        retryButton = tk.Button(retryWindow, text="Retry", width=20, command=generatePlayerOneWindow).place(x=180,y=100)
        quitButton = tk.Button(retryWindow, text="Quit", width=20, command=destroyWindow).place(x=180,y=150)


def game(): # generates spinboxes
    global var1,var2,var3,var4,var5,var6,var7
    var1 = tk.StringVar()
    var2 = tk.StringVar()
    var3 = tk.StringVar()
    var4 = tk.StringVar()
    var5 = tk.StringVar()
    var6 = tk.StringVar()
    var7 = tk.StringVar()
    yValue = 40
    infoLabel3 = tkinter.Label(gameWindow, text="Guess the word", font=('Helvatical bold',20)).place(x=170, y=-2)
    for i in range(wordLength):
        if i == 0:
            sb = tk.Spinbox(gameWindow, values=Letters, textvariable=var1, ).place(x=200, y=yValue)
            yValue += 50
        elif i == 1:
            sb = tk.Spinbox(gameWindow, values=Letters, textvariable=var2).place(x=200, y=yValue)
            yValue += 50
        elif i == 2:
            sb = tk.Spinbox(gameWindow, values=Letters, textvariable=var3).place(x=200, y=yValue)
            yValue += 50
        elif i == 3:
            sb = tk.Spinbox(gameWindow, values=Letters, textvariable=var4).place(x=200, y=yValue)
            yValue += 50
        elif i == 4:
            sb = tk.Spinbox(gameWindow, values=Letters, textvariable=var5).place(x=200, y=yValue)
            yValue += 50
        elif i == 5:
            sb = tk.Spinbox(gameWindow, values=Letters, textvariable=var6).place(x=200, y=yValue)
            yValue += 50
        elif i == 6:
            sb = tk.Spinbox(gameWindow, values=Letters, textvariable=var7).place(x=200, y=yValue)
            yValue += 50
    checkButton = tk.Button(gameWindow, text="guess", height=1, width=20 ,command=commandCheckButton).place(x=190, y=yValue)

def convertToList(string): # converts the right answer to a list
    global wordlist
    wordlist = []
    wordlist[:0]=string
    return wordlist

def confirmButton(): # checks game configuration
    global gameWindow,wordLength, standardScore
    wordEntryCheck = wordEntry.get()
    wordLength = len(wordEntryCheck)
    upperWord = wordEntryCheck.upper()
    standardScore = wordLength * wordLength
    if wordEntryCheck.isalpha() and wordLength <= 7 and wordLength >= 4:
        daEpicWindow.destroy()
        gameWindow = tk.Tk()
        gameWindow.title("Game window (Player 2)")
        gameWindow.geometry("500x500")
        convertToList(upperWord)
        game()
    elif wordLength == 0:
        messagebox.showinfo("ERROR", "Please enter a word")
        wordEntry.delete(0, END)
    elif wordLength <=3 or wordLength >= 8:
        messagebox.showinfo("INFO", "Please enter 4 to 7 letters")
        wordEntry.delete(0, END)
    else:
        messagebox.showinfo("ERROR", "Please use only letters")
        wordEntry.delete(0, END)
    

def generatePlayerOneWindow(): # generates the configuration window
    global wordEntry, daEpicWindow
    try:
        retryWindow.destroy()
    except:
        pass
    daEpicWindow = tk.Tk()
    daEpicWindow.geometry("500x500")
    daEpicWindow.title("configuration window (Player 1)")
    infoLabel1 = tkinter.Label(daEpicWindow, text="Type a word")
    infoLabel1.place(relx=.5, rely=0.01, anchor="center")

    wordVar = tkinter.StringVar(value="")
    wordEntry = tkinter.Entry(daEpicWindow, textvariable=wordVar)
    wordEntry.place(relx=.5, rely=0.05, anchor="center")
    infoLabel2 = tkinter.Label(daEpicWindow, text="4 - 7 characters").place(relx=.5, rely=0.09, anchor="center")
    startButton = tkinter.Button(daEpicWindow, text="confirm",command=confirmButton).place(relx=.5, rely=0.14, anchor="center")
    daEpicWindow.mainloop()

generatePlayerOneWindow()