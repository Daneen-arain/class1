from tkinter import *
from datetime import date

def calculate_age():
    birth_year = int(entry.get())
    current_year = date.today().year
    age = current_year - birth_year
    result_label.config(text=f"You are {age} years old")

window = Tk()
window.title("Age Calculator")
window.geometry("300x150")

Label(window, text="Enter your birth year:").pack()
entry = Entry(window)
entry.pack()

Button(window, text="Calculate Age", command=calculate_age).pack()
result_label = Label(window, text="")
result_label.pack()

window.mainloop()
