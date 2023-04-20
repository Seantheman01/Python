from functies import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox # if you want to send messages to the user.

# functions
def score_retourneren(text: str) -> int:
    if getNumberOfWords(text) <= 7:
        return("5")
    elif getNumberOfWords(text) == 8:
        return("6")
    elif getNumberOfWords(text) == 9:
        return("7")
    elif getNumberOfWords(text) == 10:
        return("8")
    elif getNumberOfWords(text) == 11:
        return("11")
    elif getNumberOfWords(text) > 11:
        return("12")

def calculate():
    textToBeCalculated = calculateInput.get('1.0', 'end') # get all the text from inputfield
    characterLabel.config(text=f"Karakter: {getNumberOfCharacters(textToBeCalculated)}")
    wordsLabel.config(text=f"Woorden: {getNumberOfWords(textToBeCalculated)}")
    sentencesLabel.config(text =f"Zinnen: {getNumberOfSentences(textToBeCalculated)}")
    scoreLabel.config(text =f"AVI score: {score_retourneren(textToBeCalculated)}")

#variables TK
root = tk.Tk()              # create tkInter window
root.title('Text analyser') # set title
root.geometry('600x600')    # set dimension
calculateInput = tk.Text(root, width = 70, height = 30, background='lightgrey')       # generate imput element
calculateButton = ttk.Button(root, text='Bereken score(s)', command=calculate)        # generate button when pressed -> calculate
characterLabel = tk.Label(root, text=f'Karakters:', width=20, bg='black', fg='white') # generate characterLabel
wordsLabel = tk.Label(root, text=f'Woorden:', width=20, bg='black', fg='white')       # generate wordsLabel
sentencesLabel = tk.Label(root, text=f'Zinnen:', width=20, bg='black', fg='white')    # generate sentencesLabel
scoreLabel = tk.Label(root, text=f'AVI score:', width=20, bg='black', fg='white')        # generate scoreLabel

calculateInput.place(x=20, y=20)   # place is one of the ways to put elements on root (window).
calculateButton.place(x=20, y=520)
characterLabel.place(x=140, y=560)
wordsLabel.place(x=280, y=560)
sentencesLabel.place(x=0, y=560)
scoreLabel.place(x=420, y=560)

# start program
root.mainloop() # runs until stopped with default stop button.