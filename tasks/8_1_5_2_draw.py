def mezot_rajzol(row, column):
	for sor in range(3):
		for oszlop in range(6):
			if sor == row and oszlop == column:
				print("+ ", end="")
			else:
				print("0 ", end="")
		print()

row = int(input("Give me the row:"))
column = int(input("Give me the column:"))
while row > 0 and column > 0:
    mezot_rajzol(row-1, column-1)

    row = int(input("Give me the row:"))
    column = int(input("Give me the column:"))

print("Have nice day!")