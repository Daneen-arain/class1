import random

# Simulated background and sound
print("🪐 Background: Galaxy loaded")
print("🔊 Sound: Laser pew pew sound loaded")

# Game variables
player_position = 0
enemy_position = random.randint(1, 10)
score = 0

print("Welcome to Space Invader - Part 2!")
print(f"Enemy is at position {enemy_position}")

# Game logic
player_position = int(input("Enter a position to shoot (1-10): "))

if player_position == enemy_position:
    score += 1
    print("🎯 Direct Hit! Score increased.")
else:
    print("💨 Missed!")

print(f"Total Score: {score}")
