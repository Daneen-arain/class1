from tkinter import *

# Function to calculate interest
def calculate_interest():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())

    simple = (p * r * t) / 100
    compound = p * ((1 + r / 100) ** t) - p

    result_label.config(
        text=f"Simple Interest: ${simple:.2f}\nCompound Interest: ${compound:.2f}"
    )

# Setup GUI
root = Tk()
root.title("Interest Calculator")
root.geometry("400x300")

Label(root, text="Principal Amount:", font=("Arial", 11)).pack(pady=5)
principal_entry = Entry(root)
principal_entry.pack()

Label(root, text="Rate of Interest (%):", font=("Arial", 11)).pack(pady=5)
rate_entry = Entry(root)
rate_entry.pack()

Label(root, text="Time (years):", font=("Arial", 11)).pack(pady=5)
time_entry = Entry(root)
time_entry.pack()

Button(root, text="Calculate Interest", command=calculate_interest).pack(pady=15)

result_label = Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
