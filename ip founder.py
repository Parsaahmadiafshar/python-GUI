from tkinter import *
from socket import *

win = Tk()
win.title('find IP')
win.geometry("200x200")
win.resizable()
win.configure(background="gray")

def ip():
    name = n.get()
    try:
        l2.configure(text=gethostbyname(name), fg="green")
    except:
        l2.configure(text="Name of Website is false", fg="yellow")

l = Label(win, text="Enter Domain: ", fg ="blue",bg="white")
l.grid()

n = StringVar()

e = Entry(win, width=32, textvariable=n)
e.grid()

b = Button(win, text="Ckeck Ip", bg="blue", command=ip)
b.grid()

l2 = Label(win, text="", fg="red", bg="gray")
l2.grid()


win.mainloop()
