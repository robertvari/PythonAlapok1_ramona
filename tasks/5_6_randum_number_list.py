import random

random_numbers = []

# generate 20 random numbers
count = 0
while count < 20:
    count += 1
    random_numbers.append(random.randint(1,12))

found = 0
# print all numbers that can be divided by 3
found = 0
for item in random_numbers:
    if item % 3 == 0:
        print(item)
        found += 1

print(f"We found {found} numbers that can be divided with 3")