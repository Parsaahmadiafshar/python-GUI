from tkinter import *

win = Tk()
win.geometry("200x200")
win.resizable()
win.configure(background="blue")
l1 = Label(text="parsa", bg='orange')
def press():
    l1.config(text="Hello world!")
b1 = Button(text="Hello world!", command=press).pack(side='right')
l1.pack()
def press2():
    l1.config(text="How are you?")
b1 = Button(text="How are you?", command=press2).pack(side='left')
l1.pack()
win.mainloop()
