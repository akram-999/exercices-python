notes_lenght= int(input("enter the numbers lenght:"))

notes=[]

for i in range(notes_lenght):
    note = int(input(f"Enter note{i + 1}: "))
    notes.append(note)

    list_notes = notes
    numbers_pairs = [x for x in list_notes if x % 2 == 0]
    numbers_impairs = [x for x in list_notes if x % 2 != 0]
    average_pairs = sum(numbers_pairs) / len(numbers_pairs) if numbers_pairs else 0
    average_impairs = sum(numbers_impairs) / len(numbers_impairs) if numbers_impairs else 0

print(f"List of notes: {list_notes}")
print(f"Pairs: {numbers_pairs}")
print(f"Impairs: {numbers_impairs}")
print(f"Average of pairs: {average_pairs}")
print(f"Average of impairs: {average_impairs}")