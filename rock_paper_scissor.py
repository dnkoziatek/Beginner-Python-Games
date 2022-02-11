# ************************************** Rock Paper Scissors Game! **************************************

import random

def RPS_game ():

    print("Now to play Rock, Paper, Scissors!")
    play_again = "Y"

    while play_again == "Y":
        user_choice = input("Type 'R' for rock, 'P' for paper, and 'S' for scissors: ")

        #Change users guess if they didn't pick one of the options
        if (user_choice != "R") and (user_choice != "P") and (user_choice != "S"):
            print("You didn't choose correctly... You're a rock.")
            user_choice = "R"

        computer_choice = random.choice(['R', "P", "S"])
        print(f"Computer's choice is: {computer_choice}.")


        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice =="R") and (computer_choice == "P"):
            print("Computer wins!")
        elif (user_choice =="R") and (computer_choice == "S"):
            print("You win!")
        elif (user_choice =="P") and (computer_choice == "R"):
            print("You win!")
        elif (user_choice =="P") and (computer_choice == "S"):
            print("Computer wins!")
        elif (user_choice =="S") and (computer_choice == "P"):
            print("You win!")
        elif (user_choice =="S") and (computer_choice == "R"):
            print("Computer wins!")

        #Play again input
        play_again = "N"
        play_again = input("Type 'Y' to play again: ")

RPS_game()
