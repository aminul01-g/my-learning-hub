<div align="center">

🐍 Aminul's Python Project Showcase 🐍
<p>
A curated collection of my Python projects, ranging from fun command-line games to practical utilities. This repository showcases my journey and skills in Python development.
</p>

<p>
<a href="https://github.com/aminul01-g/pythonProjects/blob/main/LICENSE">
<img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
</a>
</p>

</div>

📚 Table of Contents
Project 1: 🧠 Quiz Game

Project 2: 🔢 Number Guesser

Project 3: 🗿 Rock, Paper, Scissors

Project 4: 🗺️ Choose Your Own Adventure

Project 5: 🔒 Password Manager

Project 6: 🖼️ QR Code Generator

🛠️ How to Run

🤝 Contributing

🧠 Project 1: Quiz Game
A simple, interactive quiz game that tests your knowledge of computer hardware acronyms.

Key Features:

✅ Asks multiple-choice questions one by one.

✅ Validates user answers (case-insensitive).

✅ Tracks and displays the final score and percentage.

Technologies Used:

<details>
<summary>Click to view code</summary>

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

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/question)*100) + "%.")

</details>

🔢 Project 2: Number Guesser
A classic number guessing game where the user tries to guess a randomly generated number within a range they define.

Key Features:

⬆️ User-defined upper limit for the number range.

🎲 Random number generation.

💬 Provides "higher" or "lower" feedback to guide the user.

🏆 Counts the total number of guesses taken to win.

Technologies Used:

<details>
<summary>Click to view code</summary>

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

</details>

🗿 Project 3: Rock, Paper, Scissors
The timeless game of Rock, Paper, Scissors played against the computer. The game continues until the user decides to quit.

Key Features:

🤖 Play against a computer with randomized choices.

📊 Keeps track of both user and computer wins.

⌨️ Simple and intuitive command-line interface.

Technologies Used:

<details>
<summary>Click to view code</summary>

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

</details>

🗺️ Project 4: Choose Your Own Adventure
A text-based adventure game where your choices determine the outcome. Navigate through a story by making decisions that lead to different paths and endings.

Key Features:

🌳 A branching narrative based on user input.

🔚 Multiple story paths and unique endings.

✨ Engaging and interactive storytelling.

Technologies Used:

<details>
<summary>Click to view code</summary>

#Choose Your Own Adventure
#This is a Choose Your Own Adventure project
#This project is created by Md Aminul islam Bhuiyan
#Date: 2025-Jan-16
name = input("Type youre name: ")
print("Welcome ",name," to this adventure!")

answer = input("\n> You are on a dirt road, it has come to end you can go left or right. which way would you like to go? ").lower()

if answer == "left":
    answer = input("\n> You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
         print("\n_You swam acrross and were eaten by an alligator.")
    elif answer == "walk":
         print("\n_You walked for many miles, ran out of water and you lost the game.")
    else:
        print("\n_Not a valid option. You lose.")

elif answer == "right":
    answer = input("\n> You come to a bridge, it looks wobbly, do you want to cross or head back (cross/back)? ")
    if answer == "back":
         print("\n_You go back and lose.")
    elif answer == "cross":
         answer = input("\n> You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

         if answer == "yes":
            print("\n_You talk to the stranger and they give you gold. YOU WIN!")
         elif answer =="no":
            print("\n_You ignore the stranger and they are offended and you lose.")
    else:
        print("\n_Not a valid option. You lose.")
else:
    print("\n_Not a valid option. You lose.")

print("\nThank you for trying", name)

</details>

🔒 Project 5: Password Manager
A command-line tool to securely store and retrieve account passwords. It uses the cryptography library to encrypt passwords before saving them locally.

Key Features:

➕ Add new account credentials.

👀 View all stored credentials.

🔐 Encrypts passwords for secure local storage.

🔑 Generates and uses a secret key for encryption.

Technologies Used:

cryptography

<details>
<summary>Click to view code</summary>

#Password Manager
#This is a Medium level project
#This project is created by Md Aminul islam Bhuiyan
#Date: 2025-Jan-17
from cryptography.fernet import Fernet

# Generate a new key
key = Fernet.generate_key()
fer = Fernet(key)

# Save the key to a file for later use
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

</details>

🖼️ Project 6: QR Code Generator
A handy utility that generates a QR code from any text or URL provided by the user and saves it as a PNG image file.

Key Features:

🔗 Encodes any string (text or URL) into a QR code.

🎨 Customizable QR code appearance (box size, border).

💾 Saves the final QR code as a qr_code.png image.

Technologies Used:

qrcode

<details>
<summary>Click to view code</summary>

#Generate a QR code
#This is a Medium level project
#This project is created by Md Aminul islam Bhuiyan
#Date: 2025-Jan-19
import qrcode

def generate_qr_code(text, file_name):
    '''
    Generates a QR code from the given text and saves it as an image file.

    Parameters:
    text (str): The text or URL to encode in the QR code.
    file_name (str): The name of the file where the QR code image will be saved.
    '''
    try:
        qr = qrcode.QRCode(
            version = 1,
            error_correction= qrcode.constants.ERROR_CORRECT_L,
            box_size= 10,
            border=3
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color = "#000000", back_color = "White")
        img.save(file_name)
        print(f"QR code successfully saved as {file_name}")
    except Exception as e:
        print(f"An error occurred:{e}")

if __name__ == "__main__":
    # text = "https://github.com/aminul01-g/pythonProjects"
    text = input("Input Your URL or Text: ")
    file_name = "qr_code.png"

    generate_qr_code(text, file_name)
    print(f"QR code saved as {file_name}")

</details>

🛠️ How to Run
1. Clone the Repository
git clone https://github.com/aminul01-g/pythonProjects.git
cd pythonProjects

2. Install Dependencies (if needed)
Most projects use Python's standard library. For projects that require external libraries, install them using pip:

# For Password Manager
pip install cryptography

# For QR Code Generator
pip install qrcode[pil]

3. Run the Python Script
Execute the desired project file from your terminal. For example:

python "Rock, Paper, Scissors.py"

Or for the QR Code Generator:

python "Generate a QR code.py"

🤝 Contributing
Contributions, issues, and feature requests are welcome! If you have suggestions for improving any of the projects, feel free to open an issue or submit a pull request.

<div align="center">
<h3>Thank you for visiting my repository!</h3>
</div>
