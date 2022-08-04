import hashlib as f
from tkinter import *
''''
here we produce
hash code for data
'''
def hashproducer():
    num = ch.get()
    text = x.get()
    if num == 1:
        a = f.md5()
        a.update(text.encode())
        Ha = a.hexdigest()
        lable3.configure(text=f'hash-md5 :{Ha}', fg='black')
    elif num == 2:
        a = f.sha1()
        a.update(text.encode())
        Ha = a.hexdigest()
        lable3.configure(text=f'hash-sha1 : {Ha}', fg='black')
    elif num == 3:
        a = f.sha224()
        a.update(text.encode())
        Ha = a.hexdigest()
        lable3.configure(text=f'hash-sha224 : {Ha}', fg='black')
    elif num == 4:
        a = f.sha256()
        a.update(text.encode())
        Ha = a.hexdigest()
        lable3.configure(text=f'hash-sha256 : {Ha}', fg='black')
    elif num == 5:
        a = f.sha384()
        a.update(text.encode())
        Ha = a.hexdigest()
        lable3.configure(text=f'hash-sha384:{Ha}', fg='black')
    elif num == 6:
        a = f.sha512()
        a.update(text.encode())
        Ha = a.hexdigest()
        lable3.configure(text=f'hash-sha512 : {Ha}', fg='black')
    else:
        lable3.configure(text='you did\'nt select any option or data please try again', fg='green')
        'you did\'nt select any option or data please try again'
win = Tk()
win.title('Hashing programm')
win.configure(background='purple')
win.resizable(0,0)
lable1 = Label(win, text='your alghoritms for hashing ====>> 1-md5  2-sha1  3-sha224  4-sha256  5-sha384  6-sha512',
               fg="red", bg="yellow")
lable1.grid(ipadx="4", ipady="10")
lable2 = Label(win, text='please choose one of this number and plesae write taht in Entry Box', fg="black", bg="white")
lable2.grid(ipadx="4", ipady="10")
ch = IntVar()
m = Entry(win, width=32, textvariable=ch)
m.grid()
lable2 = Label(win, text='Enter your data for hashing', fg="black", bg="white")
lable2.grid(ipadx="4", ipady="10")
x = StringVar()
e = Entry(win, width=32, textvariable=x)
e.grid()
b = Button(win, text="Enter process", bg="orange", command=hashproducer)
b.grid()
lable3 = Label(win, text="", fg="red", bg="purple")
lable3.grid(ipadx="4", ipady="10")
win.mainloop()



