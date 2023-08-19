import random

numbers = []

count = 0
while count < 10:
    lucky_number = random.randint(0,50)
    if lucky_number % 4 == 0:
        numbers.append(lucky_number)
    count+=1

print(numbers, f"The length of the list is: {len(numbers)}")