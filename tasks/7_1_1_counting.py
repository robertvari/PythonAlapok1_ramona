import random

# create an empty list for storing my lucky numbers
my_lucky_numbers = []

# create a counter to drive my while loop
count = 0  
while count < 5:  # check if cound < 5
    # get a random number between 1-10
    random_number = random.randint(1,10)

    # append my random number to my_lucky_numbers
    my_lucky_numbers.append(random_number)

    # add 1 to cound
    count += 1

# print my_lucky_numbers
print(my_lucky_numbers)

# count all even numbers in my_lucky_numbers
even_numbers = 0
for item in my_lucky_numbers:
    if item % 2 == 0:
        even_numbers += 1

# print how many even numbers we found
print(f"I found {even_numbers} even numbers.")