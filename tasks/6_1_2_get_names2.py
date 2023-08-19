# get the first name
name = input("Give me a name:")

# create an empty list for the names
my_friends = []

# start a loop and check name length
number = 0
while len(name) != 0:
    number += 1
    # add name to my_friends
    my_friends.append(name)
    
    if number == 3:
        print("You don't have more chance to give a name.")
        break

    # get a new name
    name = input("Give me a name:")

print(my_friends)
print("Exit program!")