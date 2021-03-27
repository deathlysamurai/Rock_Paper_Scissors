import random

def main():
    run = True
    while run:
        print("Welcome to rock, paper, scissors!")
        player_answer = player_choice()
        computer_answer = computer_choice()
        print("Computer: ", computer_answer)
        winner = find_winner(player_answer, computer_answer)
        if winner == "player":
            print("Congratulations you win!")
        elif winner == "computer":
            print("Computer wins, better luck next time.")
        else:
            print("TIE")
        play_again = input("Would you like to continue playing? yes or no?\n")
        while (play_again != "yes") and (play_again != "no"):
            play_again = input("Please enter yes or no to continue playing or stop.\n")
        if play_again == "no":
            run = False
        
def player_choice():
    player_answer = input("Choose your weapon\n")
    while (player_answer != "rock") and (player_answer != "paper") and (player_answer != "scissors"):
        player_answer = input("You must choose rock, paper, or scissors.\n")
    return player_answer
        
def computer_choice():
    computer_number = random.randint(1, 3)
    if computer_number == 1:
        computer_answer = "rock"
    elif computer_number == 2:
        computer_answer = "paper"
    else:
        computer_answer = "scissors"
    return computer_answer

def find_winner(player, computer):
    if (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        winner = "player"
    elif (computer == "rock" and player == "scissors") or (computer == "paper" and player == "rock") or (computer == "scissors" and player == "paper"):
        winner = "computer"
    else:
        winner = "tie"
    return winner
main()