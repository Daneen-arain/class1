try:
    number = int(input("Enter a number: "))
    print("The number entered is", number)

except ValueError as x:
    print("Exception:", x)



