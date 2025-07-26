from tkinter import *

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    product = num1 * num2
    result_label.config(text=f"Product: {product}")

window = Tk()
window.title("Multiply Numbers")
window.geometry("300x200")

Label(window, text="Enter first number:").pack()
entry1 = Entry(window)
entry1.pack()

Label(window, text="Enter second number:").pack()
entry2 = Entry(window)
entry2.pack()

Button(window, text="Multiply", command=multiply).pack()
result_label = Label(window, text="")
result_label.pack()

window.mainloop()
