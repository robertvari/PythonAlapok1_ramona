your_number = int(input("Give me an even number:"))

while your_number % 2 != 0:
    print(f"Incorrect. The number {your_number} is an odd number.")
    your_number = int(input("Give me an even number:"))

print(f"Correct. Your number {your_number} is an even number.")
