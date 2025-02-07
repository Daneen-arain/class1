costprice = int(input("Enter the CP: "))
sellingprice = int(input("Enter the SP: "))

if sellingprice > costprice:
    print("Profit")
    pt = sellingprice - costprice
    print("The profit is:", pt)
elif sellingprice == costprice:
    print("No profit no loss!")
else:
    print("No profit")
