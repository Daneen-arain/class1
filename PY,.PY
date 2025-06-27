import random

# Game variables
player_position = 0
enemy_position = random.randint(1, 10)
score = 0

# Game logic
print("Welcome to Space Invader - Part 1!")
print(f"Enemy is at position {enemy_position}")

# Simulate player moving and checking for collision
player_position = int(input("Enter a position to move player (1-10): "))

if player_position == enemy_position:
    score += 1
    print("Hit! Score increased.")
else:
    print("Missed!")

print(f"Your score: {score}")
