from tkinter import *

def get_spinbox_val():
	print(sp.get())

win = Tk() 
win.geometry("300x200") 

w = Label(win, text ='StudyTonight', fg="navyblue",font = "50") 
w.pack() 

sp = Spinbox(win, from_= 0, to = 50, command=get_spinbox_val)
sp.pack() 
# print(sp.get())

win.mainloop()