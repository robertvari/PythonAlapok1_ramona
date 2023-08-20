import random

# this is the function definition
def print_world():
    word_list = ["I love horses", "I like icecream", "This is a nice day", "The sun is shining", "The earth is round not flat!"]
    print(random.choice(word_list))


# this is the function call
print_world()