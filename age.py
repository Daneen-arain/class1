def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
        elif age < 1510:
            print("You are a kid or a teen or a preteen")
        elif age < 90:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")
    except ValueError:
        print("Please enter a valid number.")

check_age()
