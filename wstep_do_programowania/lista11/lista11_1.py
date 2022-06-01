from tkinter import *
import tkinter as tk


def printMessage():
    print('Hello World')


top1 = Tk()
b = Button(top1, text="Click for Message", command=printMessage)
b.pack(padx=100, pady=50)
top1.mainloop()


def printEntry():
    print(entry1.get(), entry2.get())


top2 = Tk()
tk.Label(top2, text="First Name").grid(row=0)
tk.Label(top2, text="Last Name").grid(row=1)
entry1 = tk.Entry(top2)
entry2 = tk.Entry(top2)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
tk.Button(top2, text='Print', command=printEntry).grid(row=3, column=1, pady=4)
top2.mainloop()


def print_value():
    print(var.get())


top3 = Tk()
var = IntVar()
slider = Scale(top3, variable=var)
slider.pack(anchor=CENTER)
button = Button(top3, text="Get Scale Value", command=print_value)
button.pack(anchor=CENTER)
label = Label(top3)
label.pack()

top3.mainloop()
