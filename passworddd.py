from tkinter import *

# Function to check password strength
def check_strength():
    password = entry.get()
    strength = "Weak"

    if len(password) >= 12:
        strength = "Strong"
    elif len(password) >= 8:
        strength = "Moderate"

    result_label.config(text=f"Password Strength: {strength}")

# Setup GUI
root = Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = Entry(root, show="*", width=30)
entry.pack()

Button(root, text="Check Strength", command=check_strength).pack(pady=10)

result_label = Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
