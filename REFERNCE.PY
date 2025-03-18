num = int(input("Enter a number: "))  # Get input from the user
count = 0

while num > 0:
    num = num // 10  # Remove the last digit
    count += 1  # Increment the count

print("Total number of digits:", count)
