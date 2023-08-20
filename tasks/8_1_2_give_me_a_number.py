def numbers(number):
    if number > 0:
        print("Your number is greater than 0")
    elif number < 0:
        print("Your number is lower than 0")
    else:
        print("Your number is 0")

give_a_number = int(input("Give me a number:"))
numbers(give_a_number)