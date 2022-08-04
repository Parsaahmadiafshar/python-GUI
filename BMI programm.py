from tkinter import *
def BMI_Rerouting():
 the_weight = n.get()
 the_height = x.get()
 the_BMI = the_weight / (the_height / 100) ** 2
 # printing the BMI
 lable3.configure(text=f"Your Body Mass Index is{the_BMI}", fg='black')
 # using the if-elif-else conditions
 if the_BMI <= 18.5:
  lable3.configure(text="Oops! You are underweight.", fg='black')
 elif the_BMI <= 24.9:
  lable3.configure(text="Awesome! You are healthy.", fg='black')
 elif the_BMI <= 29.9:
  lable3.configure(text="Eee! You are over weight.", fg='black')
 else:
  lable3.configure(text="Seesh! You are obese.", fg='black')

win = Tk()
win.title('BMI programm')
win.geometry("300x300")
win.resizable(0,0)
win.configure(background="brown")

lable1 = Label(win, text="Enter your weight in kilograms: ", fg="red", bg="blue")
lable1.grid(ipadx="4", ipady="10")

n = IntVar()

e = Entry(win, width=32, textvariable=n)
e.grid()


lable2 = Label(win, text="Enter your height: ", fg="red", bg="blue")
lable2.grid(ipadx="4", ipady="10")

x = IntVar()
j = Entry(win, width=32, textvariable=x)
j.grid()

button1 = Button(win, text="Enter process", fg="blue",bg="yellow", command=BMI_Rerouting)
button1.grid()
lable3 = Label(win, text="", fg="green", bg="brown")
lable3.grid(ipadx="4", ipady="10")

win.mainloop()
