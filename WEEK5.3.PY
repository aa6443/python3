from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Address Entry Form")
window.geometry('400x400')

# Labels
Label(window, text="First Name : ").grid(row=2, column=0)
Label(window, text="Address Line 1 : ").grid(row=3, column=0)
Label(window, text="Address Line 2 : ").grid(row=4, column=0)
Label(window, text="City : ").grid(row=5, column=0)
Label(window, text="State/Province : ").grid(row=6, column=0)
Label(window, text="Postal Code : ").grid(row=7, column=0)
Label(window, text="Country : ").grid(row=8, column=0)

# Entries
Entry(window).grid(row=2, column=1)
Entry(window).grid(row=3, column=1)
Entry(window).grid(row=4, column=1)
Entry(window).grid(row=5, column=1)
Entry(window).grid(row=6, column=1)
Entry(window).grid(row=7, column=1)
Entry(window).grid(row=8, column=1)

# Buttons
Button(window, text="Clear").grid(row=12, column=1)
Button(window, text="Reset").grid(row=12, column=2)

window.mainloop()
