# Power calculator using loops

# Get input from the user
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Initialize result to 1
result = 1

# Loop to multiply the base exponent times
for _ in range(exponent):
    result *= base

print(f"{base} raised to the power of {exponent} is: {result}")
