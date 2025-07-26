from tkinter import *

root = Tk()
root.title("Main Window")
root.geometry("300x200")


def topwin():
    top=Toplevel()
    top.geometry("200x200")
    top.title("toplevel")
    L1=Label(top,text="this is my top level window")
    L1.pack()
    top.mainloop()

btn=Button(root,text="click here",command=topwin)
btn.pack()
root.mainloop()
