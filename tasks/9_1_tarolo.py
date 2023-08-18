"""
Írj egy programot, ami 4 darab három elemű [0;25] intervallumban lévő véletlen egész számokat tartalmazó listát generál, 
és ezeket a listákat egy 'tarolo' nevű listába helyezi. 
A program írja ki a képernyőre a 'tarolo' nevű lista tartalmát!
"""
import random

# create the container for storing my lists
tarolo = []

# create a while loop which runs 4 times
counter = 0
while counter < 4:
    # create a list with 3 items and generate a random number on each index
    my_random_numbers = [random.randint(0,25), random.randint(0,25), random.randint(0,25)]

    # add my_random_numbers to tarolo 
    tarolo.append(my_random_numbers)

    # add 1 to counter
    counter += 1

print(tarolo)