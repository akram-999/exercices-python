import random

choices = ["rock", "paper", "scissors"]

def play_game():
    computer_choice = random.choice(choices)
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return play_game()

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        return play_game()
    else:
        print("Thanks for playing!")

play_game()