print("Give a whole number between -5, 5")

valid_numbers = []

number = int(input("Your number:"))

while number <= 5 and number >= -5:
    valid_numbers.append(number)
    number = int(input("Your number:"))

print(f"Valid numbers are: {valid_numbers}. Summer of these numbers is: {sum(valid_numbers)}")