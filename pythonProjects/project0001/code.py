#Quiz_Game_project
#This is a simple quiz game project
#This project is created by Md Aminul islam Bhuiyan
#Date: 2021-09-26
print("Welcome to my computer quiz! ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
question = 0
score = 0

print("Okay! Let's play :) ")


  #Q1
answer = input("What does CPU stand for? ")
question += 1
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")


  #Q2
answer = input("What does GPU stand for ")
question += 1
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")


  #Q3
answer = input("What does RAM stand for? ")
question += 1
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print("Incorrect!")


  #Q4
answer = input("What does PSU stand for? ")
question += 1
if answer.lower() == "power supply unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

'''
  #Q5
answer = input("What does CPU stand for? ")
question += 1
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")
'''
'''
    #Q6
answer = input("What does CPU stand for? ")
question += 1
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")
'''

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/question)*100) + "%.")