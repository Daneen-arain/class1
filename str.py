# Input a word or sentence
string = input("Please enter your own String: ")

string2 = ''  # Empty string for reversed output

# Loop for printing in reverse
for i in string:
    string2 = i + string2  # Prepend each character

print("\nThe Original String =", string)
print("The Reversed String =", string2)