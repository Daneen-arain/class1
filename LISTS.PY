# Square it Out! Lesson 11 - Getting Started with Lists

# Ask the user for the start and end of the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Create a list of square values
squares = [num**2 for num in range(start, end + 1)]

# Separate the square values into odd and even
even_squares = [sq for sq in squares if sq % 2 == 0]
odd_squares = [sq for sq in squares if sq % 2 != 0]

# Display the results
print("\nAll Square Numbers:", squares)
print("Even Square Numbers:", even_squares)
print("Odd Square Numbers:", odd_squares)
