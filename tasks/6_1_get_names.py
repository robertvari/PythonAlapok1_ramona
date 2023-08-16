# get the first name
name = input("Give me a name:")

# create an empty list for the names
my_friends = []

# start a loop and check name length
while len(name) != 0:
    # add name to my_friends
    my_friends.append(name)

    # get a new name
    name = input("Give me a name:")

print(my_friends)
print("Exit program!")