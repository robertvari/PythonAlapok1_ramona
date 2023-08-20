import random
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

my_favorite_day = random.choice(days)
print(f"HINT: {my_favorite_day}")

question = input("What is my favorite day?")
while my_favorite_day != question:
    print("Wrong!")
    question = input("What is my favorite day?")

print(f"Good answer! My favorite day is {my_favorite_day}.")