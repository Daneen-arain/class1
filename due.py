# Get input from the user
total_bill = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid: "))

# Calculate the due amount
due_amount = total_bill - amount_paid

# Display the result
if due_amount > 0:
    print(f"The due amount is: ${due_amount:.2f}")
elif due_amount < 0:
    print(f"Overpaid! Change to return: ${abs(due_amount):.2f}")
else:
    print("The bill is fully paid. No due amount.")
