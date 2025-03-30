def check_age():
    try:
        age = int(input("Enter your age: "))

        # Check if age is within a reasonable range
        if age < 0 or age > 120:
            print("Invalid age entered. Please enter a number between 0 and 120.")
            return

        # Check if age is even or odd
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

check_age()
