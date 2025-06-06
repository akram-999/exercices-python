import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
