
string = input("Please enter your own word: ")


char = input("Please enter your own character: ")

count = 0  
for i in range(len(string)):
    if string[i] == char:  
        count += 1

print("The total number of times", char, "has occurred =", count)
      

