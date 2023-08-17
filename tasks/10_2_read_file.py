# r = raw string
file_name = r"D:\Work\_PythonSuli\Maganoktatas\Alapok1\tasks\Sherlock_Holmes.txt"

file = open(file_name, encoding="utf8")
file_content = file.read()

character_number = len(file_content)
world_count = len(file_content.split())

# collect hungarian vowels
vowels = ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]

# create a counter for count vowels
vowel_count = 0

# step over all letters in file_content
for item in file_content:
    # check it item in vowels
    if item.lower() in vowels:
        # add 1 to vowel_count
        vowel_count += 1


print(f"Character count: {character_number}")
print(f"Word count: {world_count}")
print(f"Vowel count: {vowel_count}")

file.close()