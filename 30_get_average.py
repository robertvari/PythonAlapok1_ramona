my_notes = [1, 2, 3, 1, 1, 2]
your_notes = [4, 5, 3, 4, 5]
csaba_notes = [3, 4, 4, 3, 5, 5, 4, 4, 4]
kriszta_notes = [5, 4, 4, 5, 5, 5, 4, 5]


def get_average(notes):
    return sum(notes) / len(notes)

result = get_average(csaba_notes)
print(result)