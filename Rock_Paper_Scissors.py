#YouTube channel 5starcoder
#subscribe my channel 
#project_02

import random
# List of choices
choices = ['Rock', 'Paper', 'Scissors']

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win! 🏆"
    else:
        return "You lose! 🤦‍♂️"

# Main game loop
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        # Get player's choice
        player_choice = input("Enter Rock, Paper, or Scissors (or 'quit' to exit): ").capitalize()
        if player_choice == 'Quit':
            print("Thanks for playing!")
            break
        elif player_choice not in choices:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        # Get computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine and display the result
        result = determine_winner(player_choice, computer_choice)
        print(result)

# Run the game
play_game()
