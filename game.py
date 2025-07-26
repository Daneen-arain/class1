from tkinter import *
import random
import time

score = 0
start_time = 0

heart_styles = [
    ("💗", "lavender"),
    ("💓", "black"), 
    ("💘", "green"),
    ("💝", "blue"),
    ("💖", "red"),
    ("❤️", "yellow"),
    ("🩷", "pink"),
    ("🧡", "orange")
]

def start_game():
    global start_time, score
    score = 0
    start_time = time.time()
    score_label.config(text="Score: 0")
    move_heart()

def move_heart():
    global score
    if time.time() - start_time < 10:
        x = random.randint(50, 250)
        y = random.randint(50, 200)
        emoji, color = random.choice(heart_styles)
        heart_button.config(text=emoji, bg=color, activebackground=color)
        heart_button.place(x=x, y=y)
        root.after(700, move_heart)
    else:
        heart_button.place_forget()
        score_label.config(text=f"Time's up! Final Score: {score}")

def click_heart():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")

root = Tk()
root.title("💗 Colorful Heart Clicker 💗")
root.geometry("400x300")
root.configure(bg="pink")

Label(root, text="Click the 💗 as fast as you can!", font=("Arial", 14), bg="pink").pack(pady=10)

score_label = Label(root, text="Score: 0", font=("Arial", 12, "bold"), bg="pink")
score_label.pack()

heart_button = Button(root, text="💗", font=("Arial", 24), command=click_heart)
heart_button.place_forget()

start_btn = Button(root, text="Start Game", font=("Arial", 12), bg="white", command=start_game)
start_btn.pack(pady=20)

root.mainloop()
