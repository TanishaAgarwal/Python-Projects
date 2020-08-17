
from tkinter import *
from functools import partial
from tkinter import messagebox



win=Tk()

win.geometry('700x500')
def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

frame = Frame(win)
frame.grid()

bottomframe = Frame(win)
bottomframe.grid()

B1 = Button(bottomframe, text ="1", command = helloCallBack)
B1.grid(row=2, column=1)
B2 = Button(bottomframe, text ="2", command = helloCallBack)
B2.grid(row=1, column=2)
B3 = Button(bottomframe, text ="3", command = helloCallBack)
B3.grid(row=1, column=3)
B4 = Button(bottomframe, text ="4", command = helloCallBack)
B1.grid(row=2, column=1)
B5 = Button(bottomframe, text ="5", command = helloCallBack)
B2.grid(row=2, column=2)
B6 = Button(bottomframe, text ="6", command = helloCallBack)
B3.grid(row=2, column=3)
B7 = Button(bottomframe, text ="7", command = helloCallBack)
B7.grid(row=3, column=1)
B8 = Button(bottomframe, text ="8", command = helloCallBack)
B8.grid(row=3, column=2)
B9 = Button(bottomframe, text ="9", command = helloCallBack)
B9.grid(row=3, column=3)
B00 = Button(bottomframe, text ="00", command = helloCallBack)
B00.grid(row=4, column=1)
B0 = Button(bottomframe, text ="0", command = helloCallBack)
B0.grid(row=4, column=2)
B000 = Button(bottomframe, text ="000", command = helloCallBack)
B000.grid(row=4, column=3)

BM = Button(bottomframe, text ="x", command = helloCallBack)
BM.grid(row=1, column=4)
BD = Button(bottomframe, text ="/", command = helloCallBack)
BD.grid(row=2, column=4)
BS = Button(bottomframe, text ="-", command = helloCallBack)
BS.grid(row=3, column=4)
BA = Button(bottomframe, text ="+", command = helloCallBack)
BA.grid(row=4, column=4)


BCE = Button(bottomframe, text ="CE", command = helloCallBack)
BCE.grid(row=2, column=4)
BSS = Button(bottomframe, text =".", command = helloCallBack)
BSS.grid(row=3, column=4)
BAA = Button(bottomframe, text ="=", command = helloCallBack)
BAA.grid(row=4, column=4)


win.mainloop()