import random

numbers = []

count = 0
while count < 5:
    numbers.append(random.randint(1,99))
    count += 1

give_me_a_number = int(input("Give me a number between 1 and 99:"))

if give_me_a_number in numbers:
    print(f"I found your number {give_me_a_number} in my list. You Win!")
else:
    print(f"I can't found number {give_me_a_number} in my list")

print(numbers)