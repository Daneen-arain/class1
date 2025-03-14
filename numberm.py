def decimal_to_binary(n):
    return bin(n).replace("0b", "")

# Get user input
decimal_number = int(input("Enter a decimal number: "))

# Convert and display
binary_number = decimal_to_binary(decimal_number)
print(f"Binary equivalent: {binary_number}")
