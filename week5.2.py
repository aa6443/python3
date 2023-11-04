from tkinter import *
import tkinter as k

window = Tk()
window.title("Doctor Appointment App")
window.geometry('400x400')

h = Label(window, text="SIGNUP").grid(row=1, column=0)
a = Label(window, text="First Name : ").grid(row=2, column=0)
b = Label(window, text="Last Name : ").grid(row=3, column=0)
c = Label(window, text="Age : ").grid(row=4, column=0)
d = Label(window, text="Gender : ").grid(row=5, column=0)
e = Label(window, text="City : ").grid(row=6, column=0)
f = Label(window, text="Address : ").grid(row=7, column=0)
g = Label(window, text="User Name : ").grid(row=8, column=0)
i = Label(window, text="Password : ").grid(row=9, column=0)
j = Label(window, text="Verify Password : ").grid(row=10, column=0)

a1 = Entry(window).grid(row=2, column=1)
b1 = Entry(window).grid(row=3, column=1)
c1 = Entry(window).grid(row=4, column=1)
d1 = Entry(window).grid(row=5, column=1)
e1 = Entry(window).grid(row=6, column=1)
f1 = Entry(window).grid(row=7, column=1)
g1 = Entry(window).grid(row=8, column=1)
i1 = Entry(window, show="*").grid(row=9, column=1)
j1 = Entry(window, show="*").grid(row=10, column=1)

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)

btn_submit = k.Button(window, text="Submit").grid(row=12, column=1)
btn_login = k.Button(window, text="click to login").grid(row=0, column=6)

window.mainloop()
