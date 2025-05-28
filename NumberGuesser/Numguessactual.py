# actual number gueser python

import random

top_of_range = input("Enter top limit number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please enter a number next time")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0
while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time")
        continue

    if user_guess == random_number:
        print("You got it!")
        #below is printing with f string
        print(f"it took you {guesses} guesses!: <-with f str")
        #below is another print using commas insead
        print("it took you", guesses, "guesses!: with comma")
        #below one last way to print with var
        print("it took you " + str(guesses) + " guesses!: with +")
        break
    else:
        if user_guess > random_number:
            print("too high")
        else:
            print("too low")
        guesses += 1

