my_friends = ["Csaba", "Tamás", "Ákos", "Kriszta", "Timi", "Csaba", "Ákos", "Ákos"]

find_name = "Csilla"
found = 0

for item in my_friends:
    if item == find_name:
        found += 1

if found > 0:
    print(f"I found {find_name} {found} times in friend list.")
else:
    print(f"I couldn't find {find_name} in friends list.")