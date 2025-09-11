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