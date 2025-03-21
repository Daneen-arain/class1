def shutdown(command):
    if command.lower() == "yes":
        return "Shutting down..."
    elif command.lower() == "no":
        return "Shutdown aborted!"
    else:
        return "Sorry, I didn't understand that."

# Example usage
user_input = input("Do you want to shut down? (yes/no): ")
print(shutdown(user_input))
