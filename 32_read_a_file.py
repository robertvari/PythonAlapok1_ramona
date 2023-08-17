file_name = "my_favorite_quote.txt"

# open file in memory
file = open(file_name)

# read the file content
file_content = file.read()

# print file content
print(file_content)

# important!!! Close the file
file.close()