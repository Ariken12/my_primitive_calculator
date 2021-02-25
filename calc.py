import tkinter
from tkinter import *

buth = 3
butw = 3
string = ""
before = ''

root = Tk(screenName="calculator")
root.title("calculator")

text = Label(root, text=string, height=2, width=8, font='Arial 14', bg="black", fg="white")


def moveadd1():
    global string
    global text
    string += "1"
    text.configure(text=string)


def moveadd2():
    global string
    global text
    string += "2"
    text.configure(text=string)


def moveadd3():
    global string
    global text
    string += "3"
    text.configure(text=string)


def moveadd4():
    global string
    global text
    string += "4"
    text.configure(text=string)


def moveadd5():
    global string
    global text
    string += "5"
    text.configure(text=string)


def moveadd6():
    global string
    global text
    string += "6"
    text.configure(text=string)


def moveadd7():
    global string
    global text
    string += "7"
    text.configure(text=string)


def moveadd8():
    global string
    global text
    string += "8"
    text.configure(text=string)


def moveadd9():
    global string
    global text
    string += "9"
    text.configure(text=string)


def moveadd0():
    global string
    global text
    string += "0"
    text.configure(text=string)

def moveaddplus():
    global string
    global text
    string += "+"
    text.configure(text=string)

def moveaddminus():
    global string
    global text
    string += "-"
    text.configure(text=string)

def equal():
    global string
    global text
    string = str(eval(string))
    text.configure(text=string)

button1 = Button(root, text='1', width=butw, height=buth, command=moveadd1)
button2 = Button(root, text="2", width=butw, height=buth, command=moveadd2)
button3 = Button(root, text="3", width=butw, height=buth, command=moveadd3)
button4 = Button(root, text="4", width=butw, height=buth, command=moveadd4)
button5 = Button(root, text="5", width=butw, height=buth, command=moveadd5)
button6 = Button(root, text="6", width=butw, height=buth, command=moveadd6)
button7 = Button(root, text="7", width=butw, height=buth, command=moveadd7)
button8 = Button(root, text="8", width=butw, height=buth, command=moveadd8)
button9 = Button(root, text="9", width=butw, height=buth, command=moveadd9)
button0 = Button(root, text="0", width=butw, height=buth, command=moveadd0)
buttonplus = Button(root, text="+", width=butw, height=buth, command=moveaddplus)
buttonminus = Button(root, text="-", width=butw, height=buth, command=moveaddminus)
buttonequal = Button(root, text="=", width=buth, height=butw, command=equal)

text.grid(row=0, column=1, columnspan=3)
button0.grid(row=4, column=2, in_=root)
button1.grid(row=1, column=1, in_=root)
button2.grid(row=1, column=2, in_=root)
button3.grid(row=1, column=3, in_=root)
button4.grid(row=2, column=1, in_=root)
button5.grid(row=2, column=2, in_=root)
button6.grid(row=2, column=3, in_=root)
button7.grid(row=3, column=1, in_=root)
button8.grid(row=3, column=2, in_=root)
button9.grid(row=3, column=3, in_=root)
buttonplus.grid(row=4, column=1, in_=root)
buttonminus.grid(row=4, column=3, in_=root)
buttonequal.grid(row=1, column=4, in_=root)

root.mainloop()
input()
