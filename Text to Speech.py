# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:33:33 2020

@author: Nishith
"""
import tkinter as tk
from gtts import gTTS
from playsound import playsound

win = tk.Tk()
win.title("Text TO Speech")
win.geometry("400x400")


def text_to_speech():
    text = entry.get()
    speech = gTTS(text=text, lang="en")
    speech.save(r'C:\Users\Nishith\Downloads\speech.mp3')
    playsound(r'C:\Users\Nishith\Downloads\speech.mp3')


label = tk.Label(win, text="Enter Here: ")
label.grid(row=0, column=0)

entry = tk.Entry(win)
entry.grid(row=1, column=0)

button = tk.Button(win, text="Go", command=text_to_speech)
button.grid(row=1, column=1)

win.mainloop()
