from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("200x150")

def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe button was clicked!")
    button.config(bg="lightgreen", fg="black")


button = Button(text="Click me! and you wont stop", bg="red", fg="black", activebackground="green", activeforeground="green")
button.pack(pady=20)
button.bind("<Button-1>", handle_click)

window.mainloop()
