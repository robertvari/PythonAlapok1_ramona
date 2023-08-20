word = "I love horses"
letter = input("Give me a letter:")

count=0
for item in word:
    if letter.lower() == item.lower():
        count+=1

if count > 0:
    print(f"I found your letter '{letter}' {count} times")
else:
    print("Sorry, i couldn't find your letter.")

print(word)