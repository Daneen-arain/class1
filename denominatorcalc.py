from tkinter import *

def calculate_denominations():
    try:
        amount = int(entry_amount.get())
        if amount < 0:
            result_label.config(text="Enter a positive amount.")
            return

        note_2000 = amount // 2000
        amount %= 2000

        note_500 = amount // 500
        amount %= 500

        note_100 = amount // 100
        amount %= 100

        result = f"2000 Notes: {note_2000}\n500 Notes: {note_500}\n100 Notes: {note_100}"
        if amount > 0:
            result += f"\nRemaining ₹: {amount} (Cannot be split)"

        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Enter a valid number!")

# GUI setup
window = Tk()
window.title("Denomination Calculator")
window.geometry("300x300")
window.config(bg="#f0f0f0")

label = Label(window, text="Enter Amount (₹):", font=("Arial", 12), bg="#f0f0f0")
label.pack(pady=10)

entry_amount = Entry(window, font=("Arial", 12))
entry_amount.pack(pady=5)

calculate_button = Button(window, text="Calculate", command=calculate_denominations, font=("Arial", 12), bg="#4CAF50", fg="white")
calculate_button.pack(pady=10)

result_label = Label(window, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=20)

window.mainloop()
