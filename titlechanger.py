from tkinter import *

window = Tk()
window.title("GOOD MORNING MY MONKEY")
window.geometry("200x100")

def change_title():
    window.title("GOOD NIGHT MONKEY (AKA MY SISTER)")

button = Button(window, text="Change Title", command=change_title)
button.pack(pady=20)

window.mainloop()