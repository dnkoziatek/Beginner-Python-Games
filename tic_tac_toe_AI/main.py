# *********************************** Tic Tac Toe Game ***********************************
#This game is played on command prompt.
#You need python downloaded to use.
#To play, change your commmand prompt directly to where ever this folder is.
#Type: "python main.py" to start game. This may be different wording for your computer/python software.

#import functions
import random
import math
from ai import computer_ai_choice




# _______________________________ Board Winner Calculation Function _______________________________
#Check if player has a winning group!
#define board_winner function with inputs a=board list and y=player
#a is the list of values on the board. y is the player: Either 'x' or 'o'
def board_winner(a,y):
    #create winner variable to return at the end of function
    #initialize winner as false until proven true by if statements
    winner = False

    #shift through possible combinations of board that would have a board_winner
    #the board looks like:
    # a[0] | a[1] | a[2]
    # ------------------
    # a[3] | a[4] | a[5]
    # ------------------
    # a[6] | a[7] | a[8]
    if a[0]==y and a[1]==y and a[2]==y:
        winner = True
    elif a[3]==y and a[4]==y and a[5]==y:
        winner = True
    elif a[6]==y and a[7]==y and a[8]==y:
        winner = True
    elif a[0]==y and a[3]==y and a[6]==y:
        winner = True
    elif a[1]==y and a[4]==y and a[7]==y:
        winner = True
    elif a[2]==y and a[5]==y and a[8]==y:
        winner = True
    elif a[0]==y and a[4]==y and a[8]==y:
        winner = True
    elif a[2]==y and a[4]==y and a[6]==y:
        winner = True
    return winner


# _______________________________ Update Board Lists Function _______________________________
#Create function that updates board list with the input option
#b is the board
#b_taken is the taken spaces on the board.
#b_open is the open spaces on the board.
#choice is the space that's taken (1-9)
#symbol is either 'X' or 'O'
def update_board(b, b_taken, b_open, choice, symbol):
    #Update board with user's option
    #Remove space from the open board word_list
    b_open.remove(choice)
    #Add taken option to taken board word_list
    b_taken.append(choice)
    #update the current board with the space taken with the symbol
    b[choice - 1] = symbol
    #Return lists back
    return { "b": b, "b_taken": b_taken , "b_open": b_open}



# _______________________________ Tic Tac Toe Function _______________________________
#create game function tic tac toe
def tic_tac_toe():
    #initialize play_again variable. 'Y' is play__again. Anything else is exit games
    play_again = 'Y'

    #loop through game turns until winner is found or board is full.
    while play_again == 'Y':
        print("Welcome to the game of Tic Tac Toe!")
        #Create variables for the new game!
        #create list of open spaces for user/computer to pick
        board_open = [1,2,3,4,5,6,7,8,9]
        #create empty list that fills with current locations of user/computer's pieces
        board_taken = []
        #Create list that holds the current state of the board.
        #numbers are input options for the user/computer. 'x' 'o' are taken
        b = [1,2,3,4,5,6,7,8,9]
        #create boolean that holds if the game is won.
        winner = False
        winner_who = 0

        while len(board_open) and winner == False:
            print("The current board: ")
                # b[0] | b[1] | b[2]
                # ------------------
                # b[3] | b[4] | b[5]
                # ------------------
                # b[6] | b[7] | b[8]
            print(f"    {b[0]} | {b[1]} | {b[2]} ")
            print("   -----------")
            print(f"    {b[3]} | {b[4]} | {b[5]} ")
            print("   -----------")
            print(f"    {b[6]} | {b[7]} | {b[8]} ")

            #initialize user_choice so it'll loop through until user picks a viable open spot
            user_choice = 0
            #Create while loop for user to keep picking a space until its actually an option.
            while user_choice == 0:
                user_choice = input(f"You're 'X'. Type the number of a space you want to take {board_open}: ")
                #check if the input is a number (0-9)
                if user_choice.isnumeric():
                    user_choice = int(user_choice)
                #If user didn't pick an open board space, make it equal to 0 to loop again.
                if not(user_choice in board_open):
                    user_choice = 0
                    print("You picked a non-viable option. Try again.")

            #Update board lists with user's option and store in a board_updates
            board_updates = update_board(b, board_taken, board_open, user_choice, 'X')
            b = board_updates["b"]
            board_taken = board_updates["b_taken"]
            board_open = board_updates["b_open"]
            #See is if the computer just wrong
            #inputs are the current board and the symbol.
            winner = board_winner(b, 'X')
            if winner == True:
                winner_who = 1

            #print(f"Current board: {b}. Taken board spaces: {board_taken}. Open board spaces: {board_open}.")


            #allow the computer to pick a space if the user didn't win yet
            if winner == False and not(len(board_open)==0):
                #Allow the computer to pick a space and update the board Lists
                computer_choice = computer_ai_choice(b, board_open)
                print(f"Computer choice: {computer_choice}")
                board_updates = update_board(b, board_taken, board_open, computer_choice, 'O')
                b = board_updates["b"]
                board_taken = board_updates["b_taken"]
                board_open = board_updates["b_open"]
                #print(f"Current board: {b}. Taken board spaces: {board_taken}. Open board spaces: {board_open}.")

                #See is if the computer just won
                #inputs are the current board and the symbol.
                winner = board_winner(b, 'O')
                if winner == True:
                    winner_who = 2

        #Show the player the board
        print("The current board: ")
                # b[0] | b[1] | b[2]
                # ------------------
                # b[3] | b[4] | b[5]
                # ------------------
                # b[6] | b[7] | b[8]
        print(f"    {b[0]} | {b[1]} | {b[2]} ")
        print("   -----------")
        print(f"    {b[3]} | {b[4]} | {b[5]} ")
        print("   -----------")
        print(f"    {b[6]} | {b[7]} | {b[8]} ")

        if winner == True:
            if winner_who ==1:
                print("You won! Congrats!")
            elif winner_who == 2:
                print("The computer won. Good luck next time.")
        if len(board_open)==0:
            print("It is a draw. Better luck next time.")



        #Ask the player if they'd like to play again
        play_again = input("Would you like to play again? Y/N: ").upper()


tic_tac_toe()
