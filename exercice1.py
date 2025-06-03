num_notes= int(input("Enter the number of notes: "))
notes = []

for i in range(num_notes):
    note = int(input(f"Enter note {i + 1}: ")) 
    notes.append(note)

    average_length = sum(notes) / len(notes)
    highest = max(notes)


print(f"Average length of notes: {average_length}")
print(f"Highest note: {highest}")