def tuple_product(t):
    product = 1
    for num in t:
        product *= num
    return product

# Example
t = (2, 3, 4)
print("Product:", tuple_product(t))  # Output: Product: 24
