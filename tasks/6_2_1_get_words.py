user_input = input("Give me a word which starts with a letter 'a':")

word_list = []

while len(user_input) != 0:
    if user_input[0] == "a":
        word_list.append(user_input)
        print(f"Thank you. I added you word {user_input} to my list.")
    else:
        print("Incorrect world.")

    user_input = input("Give me a word which starts with a letter 'a':")

print(f"You words: {word_list}")