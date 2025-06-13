from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("250x250")
root.title("Super Scanner 3000")

def msg():
    messagebox.showwarning("ALERT", "Boom! Fake virus detected!\nYou're safe... for now.")

btn = Button(root, text="Scan for Virus!", font=("Comic Sans MS", 10), bg="hot pink", fg="white", command=msg)
btn.place(x=50, y=100)

root.mainloop()
