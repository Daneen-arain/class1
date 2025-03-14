
# Take input of number of units consumed from the user
units = int(input("Please enter Number of Units you Consumed: "))

# Check conditions of units consumed
# Then calculate amount and surcharge accordingly
# surcharge is the tax value

# Check for units less than 50
if units < 50:
    amount = units * 2.60
    surcharge = 25

# Check for units less than 100
elif units <= 100:
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

# Check for units less than or equal to 200
elif units <= 200:
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45

# Calculate and display the total electricity bill
amount = float(input("Enter the electricity bill amount: "))
surcharge = float(input("Enter the surcharge amount: "))

total = amount + surcharge

print("\nElectricity Bill = %.2f" % total)
