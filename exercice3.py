phrase = input("Enter a sentence: ")

character_count = {}

for character in phrase:
    if character.isalpha():
        character = character.lower()
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1


for character, count in character_count.items():
    print(f"{character}: {count}")


max_character = max(character_count, key=character_count.get)
max_count = character_count[max_character]
print(f"The character that appears the most is '{max_character}' with {max_count} occurrences.")
