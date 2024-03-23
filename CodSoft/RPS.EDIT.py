import random

def play():
    while True:
        player = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to quit: ").lower()

        if player == 'q':
            print("Thank you for playing!")
            break

        if player not in ['r', 'p', 's']:
            print("Invalid input! Please enter 'r', 'p', 's', or 'q' to quit.")
            continue

        choose = ["r", "p", "s"]
        computer = random.choice(choose)
        print(f'Your choice: {player} <=> Opponent: {computer}')

        if player == computer:
            print("It's a tie!")
        elif (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
            print("You won!")
        else:
            print("You lost! Better luck next time.")

play()

