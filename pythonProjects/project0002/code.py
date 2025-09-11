#Number_guesser
#This is a simple Number_guesser project
#This project is created by Md Aminul islam Bhuiyan
#Date: 2025-Jan-16
import random

top_of_range = input("Enter the top range number you want to guess: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print('print type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

r = random.randrange(1, top_of_range)

score = 0
while True:
    score +=1
    user_guess = input("Guesse your Number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time.')
        continue
    if r == user_guess:
        print("You got it Correct!")
        break
    else:
        if user_guess > r:
            print("You were above the number!")
        else:
            print("You were below the number!")

print("You got it in ", score, "guesses")