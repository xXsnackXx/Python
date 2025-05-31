# imports-------------
import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ")
    if user_input == "q":
        break
    if user_input not in options: 
        continue

    random_number = random.randint()
    #r rock: 0, paper: 2, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
    user_wins += 1
print("Goodbye")

