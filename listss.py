
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)


evens = [x for x in range(1, 21) if x % 2 == 0]
print("Evens:", evens)

words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print("Uppercase Words:", upper_words)

names = ["Adithi", "Akash", "Jawaid", "Daneen"]
a_names = [name for name in names if name.startswith("A")]
print("Names starting with 'A':", a_names)

text = "H3ll0 W0rld 123"
digits = [char for char in text if char.isdigit()]
print("Digits:", digits)

all_names = ["Adithi", "Akash", "Jawaid", "Daneen"]
hearts_per_letter = [[f"{char}💗" for char in name] for name in all_names]
print("Hearts for each letter in names:")
for name, hearts in zip(all_names, hearts_per_letter):
    print(f"{name}: {hearts}")

even_odd = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 11)]
print("Even or Odd:", even_odd)
