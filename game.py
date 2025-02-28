import random

options = ["rock", "paper", "scissors"]
user_points = 0
computer_points = 0

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

while True:
    print("\nRock, Paper, Scissors Game!")
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    if player_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(options)

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)

    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win this round!")
        user_points += 1
    else:
        print("Computer wins this round!")
        computer_points += 1

    print(f"Score -> You: {user_points} | Computer: {computer_points}")

    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay != "yes":
        print(f"Thanks for playing! Final Score -> You: {user_points} | Computer: {computer_points}")
        break
