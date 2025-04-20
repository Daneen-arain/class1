

import random
import string

# Function to generate a random password
def generate_password(length=10):
    letters = string.ascii_letters      # a-z + A-Z
    digits = string.digits              # 0-9
    symbols = string.punctuation        # !@#$%^&*()_+ etc.
    
    all_chars = letters + digits + symbols
    password = random.choices(all_chars, k=length)
    random.shuffle(password)  # Shuffle to make it extra random
    
    return ''.join(password)

# Function to start the challenge
def start_challenge():
    print("🎯 Welcome to the Random Password Challenge!\n")
    
    password = generate_password()
    
    print("🔐 Your password is:\n", password)
    print("⌨️ Type the password exactly as shown!\n")
    
    user_input = input("Your input: ")
    
    if user_input == password:
        print("\n✅ Great job, Daneen! You typed it correctly! You're a fast typer! 🚀")
    else:
        print("\n❌ Oops! That's not correct.")
        print("👉 The correct password was:", password)

# Start the game
start_challenge()
