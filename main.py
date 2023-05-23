import random

while True: 
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissors? ").lower()

    if player == computer:
        print(f'computer: {computer}')
        print(f'player: {player}')
        print("TIE!")

    elif player == "rock":
        if computer == "paper":
            print(f'computer: {computer}')
            print(f'player: {player}')
            print("You lose!")
        if computer == "scissors":
            print(f'computer: {computer}')
            print(f'player: {player}')
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print(f'computer: {computer}')
            print(f'player: {player}')
            print("You lose!")
        if computer == "paper":
            print(f'computer: {computer}')
            print(f'player: {player}')
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print(f'computer: {computer}')
            print(f'player: {player}')
            print("You lose!")
        if computer == "rock":
            print(f'computer: {computer}')
            print(f'player: {player}')
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again == "yes":
        print("Let's play rock, paper, scissors!")
        continue

    elif play_again == "no":
        print("Bye.")
        break
    else:
        print("Invalid response, type 'yes' or 'no'.")
