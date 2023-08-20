def mezot_rajzol(row, column):
	for sor in range(3):
		for oszlop in range(6):
			if sor == row and oszlop == column:
				print("+ ", end="")
			else:
				print("0 ", end="")
		print()

mezot_rajzol(0, 1)