from tkinter import *

def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    result_label.config(text=f"{cm:.2f} cm")

window = Tk()
window.title("Length Converter")
window.geometry("300x150")

Label(window, text="Enter length in inches:").pack()
entry = Entry(window)
entry.pack()

Button(window, text="Convert", command=convert).pack()
result_label = Label(window, text="")
result_label.pack()

window.mainloop()
