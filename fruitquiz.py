class FruitQuiz:
    def __init__(self):
        self.fruits = {"Apple": "Red", "Banana": "Yellow", "Grapes": "Purple"}

    def start_quiz(self):
        keys = list(self.fruits)
        i = int(input("Pick a number (0-2): "))
        if i not in [0, 1, 2]:
            print("Invalid.")
            return
        fruit = keys[i]
        ans = input(f"Color of {fruit}? ").strip().capitalize()
        print("Correct!" if ans == self.fruits[fruit] else f"Wrong! It's {self.fruits[fruit]}.")

FruitQuiz().start_quiz()
