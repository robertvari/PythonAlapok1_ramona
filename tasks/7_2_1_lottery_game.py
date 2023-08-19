import random

numbers = []

count = 0
while count < 5:
    lucky_number = random.randint(1,99)
    if lucky_number not in numbers:
        numbers.append(lucky_number)
        count += 1

player_numbers = input("Give me 5 numbers between 1-99 separated by ,:")
player_number_list = player_numbers.split(",")

your_winning_numbers = []
for item in player_number_list:
    if int(item) in numbers:
        your_winning_numbers.append(item)

if len(your_winning_numbers) > 0:
    print(f"Your winning numbers: {your_winning_numbers}")
else:
    print("You lost this game.")

if len(your_winning_numbers) == 5:
    print("YOU WIN LOTTERY!!!")

print(numbers)