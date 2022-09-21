#importing the random package to let the computer make a random choice
import random


#defining a function to a get choice from the player and a random choice from the computer
def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors:)")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


#defining a function to a check the win based on the choice from the player and a random choice from the computer
def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "Is is a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! you win!"
        else:
            return "Paper covers rock! you lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! you win!"
        else:
            return "scissors cuts paper! you lose."
    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! you win!"
        else:
            return "Rock smashes scissors! you lose."


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
