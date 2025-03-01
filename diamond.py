
def print_diamond(n):
    # Upper part of the diamond (pyramid)
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "".join(str(j) for j in range(1, i + 1)))
    
    # Lower part of the diamond (inverted pyramid)
    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "".join(str(j) for j in range(1, i + 1)))

# Input from the user
size = int(input("Enter  number for the diamond size: "))

# Ensure input is an odd number
if size % 2 == 0:
    print("Please enter an odd number!")
else:
    print_diamond(size)


