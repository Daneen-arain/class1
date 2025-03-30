import math

def calculate_trig_values():
    try:
        angle = float(input("Enter an angle in degrees: "))

        # Convert degrees to radians (since math functions use radians)
        radians = math.radians(angle)

        # Calculate trigonometric values
        sin_value = math.sin(radians)
        cos_value = math.cos(radians)
        tan_value = math.tan(radians)

        print(f"\nTrigonometric values for {angle}°:")
        print(f"Sin({angle}) = {sin_value:.4f}")
        print(f"Cos({angle}) = {cos_value:.4f}")
        print(f"Tan({angle}) = {tan_value:.4f}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

calculate_trig_values()
