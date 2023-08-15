import random

magic_number = random.randint(1, 10)
max_tries = 3

player_number = int( input("What is your number?") )

while magic_number != player_number:
    print("Wrong number!")

    max_tries -= 1
    if max_tries == 0:
        break

    player_number = int( input("What is your number?") )

if magic_number == player_number:
    print(f"You win! {magic_number} was my number.")
else:
    print(f"Game Over. {magic_number} was the correct number.")