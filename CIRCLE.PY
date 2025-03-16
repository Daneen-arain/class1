import math

def calculate_circumference(radius):
    """Calculate the circumference of a circle given its radius."""
    return 2 * math.pi * radius

# Example usage
radius = float(input("Enter the radius: "))
circumference = calculate_circumference(radius)
print(f"The circumference of the circle is: {circumference}")
