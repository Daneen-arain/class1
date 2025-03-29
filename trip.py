def hotel_cost(nights):
    return 140 * nights

# Define a function called plane_ride_cost that takes a string, city, as input.
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return 0  # Default case if city is not listed

# Define a function called rental_car_cost with an argument called days.
def rental_car_cost(days):
    cost = days * 40
    if days > 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost

# Define a function called trip_cost with arguments city, days, and spending_money.
def trip_cost(city, days, spending_money=0):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Cost of car rental: ", rental_car_cost(6))
print("Cost of plane ride: ", plane_ride_cost("Los Angeles"))
print("Cost of hotel room: ", hotel_cost(7))
print("Total cost of the trip: ", trip_cost("Los Angeles", 7, 500))
print("Total cost of the trip: ", trip_cost("Tampa", 6, 500))



