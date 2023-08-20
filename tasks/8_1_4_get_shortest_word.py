def find_shortest_word(words):
    word_list = words.split(",")
    
    number_list = []
    for item in word_list:
        number_list.append(len(item))

    index = number_list.index(min(number_list))
    shortest_word = word_list[index]
    print(f"The shortest word is: {shortest_word}")

print("I'm going to ask for three words")
words = input("Give me three words:")
find_shortest_word(words)