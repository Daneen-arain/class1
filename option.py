print("Select your ride: ")
print("1. Bike")
print("2. Car")

# Take input of number 1 or 2
# Select your ride
choice = int(input("Enter your choice: "))

# User entering option 1
if choice == 1:  # Condition 1 outer if statement
    print("What type of bike?")
    print("1. Scooty")
    print("2. Scooter")

    # Condition for selecting the type of bike
    choice2 = int(input("Enter your choice2: "))
    if choice2 == 1:  # Inner if statement
        print("You have selected Scooty")
    else:
        print("You have selected Scooter")
# User entering option 1
choice = int(input("Enter your choice (1 for bike, 2 for car): "))

if choice == 1:  # Condition 1 outer if statement
    print("What type of bike?")
    print("1. Scooty")
    print("2. Scooter")
    
    # Condition for selecting the type of bike
    choice2 = int(input("Enter your choice: "))
    if choice2 == 1:  # Inner if statement
        print("You have selected Scooty.")
    else:
        print("You have selected Scooter.")

# User entering option 2
elif choice == 2:  # Outer elif statement
    print("What type of car?")
    print("1. Sedan")
    print("2. XUV")
    
    choice3 = int(input("Enter your choice: "))
    
    if choice3 == 1:  # Inner if statement
        print("You have selected Sedan.")
    else:
        print("You have selected XUV.")

else:
    print("Invalid choice. Please enter 1 or 2.")

else:  # Outer else
statement print("Wrong choice!")