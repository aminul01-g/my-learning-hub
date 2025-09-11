#Rock, Paper, Scissors
#This is a simple Rock, Paper, Scissors project
#This project is created by Md Aminul islam Bhuiyan
#Date: 2025-Jan-16
import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("\nType Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        print("\nGoodbye!")
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    # rock : 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == computer_pick:
        print("Draw!")
        continue
    elif user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins +=1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins +=1
        continue
    
    else:
        print("You Lost!")
        computer_wins +=1
if user_wins > computer_wins:
    print("\n*********"+" Congratulation! You win. "+"*********")
    print("\nYou won ", user_wins, " times.")
    print("Computer won ",computer_wins," times")
elif user_wins == computer_wins:
    print("\n*********"+" Awww! Match is Draw. "+"*********")
    print("\nYou won ", user_wins, " times.")
    print("Computer won ",computer_wins," times")
    print("Let's Try Once Again!")
else:
    print("\n*********"+ " Oh NO! You lose. " +"*********")
    print("\nYou won ", user_wins, " times.")
    print("Computer won ",computer_wins," times")
    print("Let's Try Once Again!")