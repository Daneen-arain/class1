from tkinter import *

root = Tk()
root.title("Main Window")
root.geometry("300x200")

def open_new_window():
    new_window = Toplevel(root)
    new_window.title("Top Level Window")
    new_window.geometry("200x150")
    label = Label(new_window, text="This is a TopLevel window!")
    label.pack(pady=20)

btn = Button(root, text="Open Top Window", command=open_new_window)
btn.pack(pady=60)

root.mainloop()
