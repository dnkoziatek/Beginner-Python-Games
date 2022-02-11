# *********************************** Number Guessing Game ***********************************
#This game is played on command prompt.
#You need python downloaded to use.
#To play, change your commmand prompt directly to where ever this folder is.
#Type: "python main.py" to start game. This may be different wording for your computer/python software.

#first import random to generate the Number
import random

#________________________________ Pick a Game! ________________________________
#create pick_game function
#Allows the user to pick between them picking the generated number
#Or allows the user to pick a number and have the computer guess it.
def pick_game():
    #user_pick is the game that the user chooses.
    #It is defaulted to 0 so the user needs to pick 1 or 2.
    user_pick = 0;
    #max_range is the game's maximum possible number. The range is 1 to max_range
    #the default is 10.
    max_range=10;
    #Prompt the user to input which game to play.
    #'1' is the user guessing the number.
    #'2' is the computer guessing the user's number.
    user_pick = int(input("Press 1 to guess a number. Press 2 for computer to guess a number: "))

    #If the user didn't pick 1 or 2 tell them and auto choose 1.
    if (user_pick!=1) and (user_pick!=2):
        print("You didn't pick a viable game option. We're defaulting you to 1 :D")
        user_pick = 1

    #Ask user to pick the maximum range for the numbers game. 10 is the minimum number to pick.
    max_range = int(input("10 is the lowest maximum. What do you want max range to be. 1 to: "))
    #If the user input max_range less than 10 change it.
    if max_range < 10:
        max_range = 10

    #call the game function based on user's choice
    if user_pick ==1:
        guess(max_range)

    elif user_pick ==2:
        computer_guess(max_range)




#________________________________ Player Guess Number Game!  ________________________________
#Create function where the user guesses a number that the computer picked.
#x is the max_range aka the maximum number they can pick.
def guess(x):
    #Have the computer pick a random number within the specied range.
    random_number = random.randint(1,x)
    #initalize the guess to be 0 since it isn't a possibility.
    guess = 0
    #Create a loop for the user to keep guessing the number.
    #The loop continues until the user guesses the computer's number.
    while guess != random_number:
        #Prompt the user to input a guessed number.
        guess = int(input(f"Guess a number between 1 and {x}: "))
        #Print responses to the user's guess.
        # If the user guesses the correct number, tell them.
        if guess == random_number:
            print("You got it!")
        #if the user guesses a number that is lower than the computer's number, tell them.
        elif guess < random_number:
            print("Your number is too low.")
        #If the user guesses a number that is higher than the computer's number, tell them.
        elif guess > random_number:
            print("Your number is too high")



#________________________________ Computer Guess Number Game!  ________________________________
#Create function where the user picks a number that the computer is guessing.
#x is the max_range aka the maximum number they can pick.
def computer_guess(x):
    #Tell the user to pick a number within range.
    #The number isn't stored because we don't want to think we're cheating.
    print(f"Pick a number 1 - {x}: ")
    #user_ans is either 1,2,3 for how close the computer guessed.
    #The below variables are used for the computer to adjust its random number pick range.
    user_ans = 0
    #low_guess is the lowest number the picked number can be based on user_ans = 2
    #The lowest guess number to start is 1.
    low_guess = 1
    #high_guess is the highest number the picked number can be based on user_ans =3.
    #The highest guess number to start is x.
    high_guess = x

    #Create while loop. It continues until the computer guesses the user's number. Aka the user_ans = 1.
    while user_ans!=1:
        #create a computer's gueses based on the possible range.
        computer_guess = random.randint(low_guess,high_guess)
        #Tell the user the computer's guess.
        print(f"Computer guessed: {computer_guess}.")
        #Prompt the user to tell how close/right the computer's guess is.
        #'1' is the computer guessed the number
        #'2' is that the computer guessed a number lower than the picked number
        #'3' is that the computer guessed a number higher than the picked number.
        user_ans = int(input("Press 1 for Correct. 2 for too Low. 3 for too High: "))

        #check user's answer to prompt a response or adjust the computer's guessing range.
        #If user_ans says that the computer's guess is right.
        if user_ans == 1:
            print("Yey computer!")
        #If user_ans says that the computer's guess is too lower.
        elif user_ans == 2:
            #change the low_guess to be the computer's guess + 1 because that's the new possible lowest number.
            low_guess = computer_guess + 1
        #If the user_ans says that the computer's guess it too high.
        elif user_ans ==3:
            #change the high_guess to be the computer's guess - 1 because that's the new possible highest number.
            high_guess = computer_guess - 1

#Call the pick_game() function for the games to start!
pick_game()
