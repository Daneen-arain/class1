
# Take input for the student to determine if they can attend the exam or not
medical_cause = input("Did you have a medical cause? (Y or N): ").strip().upper()

# Take input for the attendance
atten = int(input("Enter the attendance of the student: "))

# Checking the user input and predicting output accordingly
if medical_cause == 'Y':  # Checking the first condition
    print("You are allowed")
else:
    if atten >= 75:  # Checking the second condition
        print("Allowed")
    else:
        print("Not allowed")
