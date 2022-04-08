from email import message
import itertools
import numbers
import string
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import END, messagebox
from tkinter.messagebox import askretrycancel, showwarning
Letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
rounds = 0
def destroyWindow():
    retryWindow.destroy()
    gameWindow.destroy()

def retry(guessedOrNot, score):
    global retryWindow, finalScore, standardScore
    retryWindow = tk.Tk()
    retryWindow.title("Retry?")
    retryWindow.geometry("500x200")
    finalScore = standardScore - wrongLetters * 2
    standardScore = finalScore
    if finalScore > 0:
        retryLabel = tk.Label(retryWindow, text=f"You {guessedOrNot} the word!.{score}\nscore: {finalScore}", font=('Helvatical bold',15)).place(x=150, y=25)
        if guessedOrNot == "guessed":
            quitButton = tk.Button(retryWindow, text="Quit", width=20, command=destroyWindow).place(x=180,y=150)
            retryButton = tk.Button(retryWindow, text="Retry", width=20, command=generatePlayerOneWindow).place(x=180,y=100)
        else:
            retryButton = tk.Button(retryWindow, text="Retry", width=20, command=game).place(x=180,y=100)
            quitButton = tk.Button(retryWindow, text="Quit", width=20, command=destroyWindow).place(x=180,y=150)
    else:
        endLabel = tk.Label(retryWindow, text=f"Je punten zijn op!\nscore: {finalScore}", font=('Helvatical bold',15)).place(x=180, y=25)
        quitButton = tk.Button(retryWindow, text="Quit", width=20, command=destroyWindow).place(x=180,y=150)
    

def checkGoodLetters():
    global correctLetters, wrongLetters
    correctLetters = 0
    wrongLetters = 0
    for i in range(wordLength):
        checkYourAnswerLetter = answer[i]
        checkAnswerLetter = upperWord[i]
        if checkYourAnswerLetter == checkAnswerLetter:
            correctLetters += 1
        else:
            wrongLetters += 1
    if wrongLetters == 0:
        retry("guessed", "")
    else:
        retry("didn't guess", f"\n You got {correctLetters} letters correct")
        standardScore = finalScore

def commandGuessButton(): # checks the given letters
    global retryWindow, answer
    answer = []
    for i in range(wordLength):
        answer.append(varList[i].get())
    while '' in answer:
        answer.remove('')
    checkGoodLetters()
    
def game(): # generates spinboxes
    global numberSpinbox, varList, rounds
    var0 = tk.StringVar(value="")
    var1 = tk.StringVar(value="")
    var2 = tk.StringVar(value="")
    var3 = tk.StringVar(value="")
    var4 = tk.StringVar(value="")
    var5 = tk.StringVar(value="")
    var6 = tk.StringVar(value="")
    varList = [var0, var1, var2, var3, var4, var5, var6]
    try:
        retryWindow.destroy()
    except:
        pass
    yValue = 40
    infoLabel3 = tkinter.Label(gameWindow, text="Guess the word", font=('Helvatical bold',20)).place(x=170, y=-2)
    numberSpinbox = 0
    yValue = 40
    for i in range(wordLength):
        numberSpinbox += 1
        spinbox = ttk.Spinbox(gameWindow, values=Letters ,textvariable=varList[i]).place(x=200, y=yValue)
        yValue += 50
    guessButton = tk.Button(gameWindow, text="guess", height=1, width=20 ,command=commandGuessButton).place(x=190, y=yValue)

def convertToList(string): # converts the right answer to a list
    global wordlist
    wordlist = []
    wordlist[:0]=string
    return wordlist

def no():
    for i in range(10):
        noWindow = tk.Tk()
        noWindow.title("no")
        noLabel = tk.Label(noWindow, text="NO").pack()
    noWindow.protocol("WM_DELETE_WINDOW", no)
def confirmButton(): # checks game configuration
    global gameWindow,wordLength, standardScore, upperWord
    wordEntryCheck = wordEntry.get()
    wordLength = len(wordEntryCheck)
    upperWord = wordEntryCheck.upper()
    standardScore = wordLength * wordLength
    if wordEntryCheck.isalpha() and wordLength <= 7 and wordLength >= 4:
        daEpicWindow.destroy()
        gameWindow = tk.Tk()
        gameWindow.title("Game window (Player 2)")
        gameWindow.geometry("500x500")
        gameWindow.protocol("WM_DELETE_WINDOW", no)
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
        gameWindow.destroy()
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