print("Reverse Half Pyramid Pattern:")
n = int(input("Enter the number of rows: "))


for i in range(n, 0, -1):
 
    for j in range(i):
        print("@", end="")
    print()  
