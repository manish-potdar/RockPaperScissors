import random

rps = ['rock', 'paper', 'scissors']

play = 'y'

while(play == 'y'):

    user_choice = int(input(" 1. Rock\n 2. Paper\n 3. Scissors\n Enter your choice : "))

    computer_choice = random.choice(rps)

    if ((computer_choice == 'rock' and user_choice == 2) or (computer_choice == 'paper' and user_choice == 3) or 
        (computer_choice == 'scissors' and user_choice == 1)):
        print("Computer choice : ", computer_choice)
        print("You win.")
        play = input("Want to play again? (y/n) : ")
    else:
        print("Computer choice : ", computer_choice)
        print("You lose.")
        play = input("Want to play again? (y/n) : ")

