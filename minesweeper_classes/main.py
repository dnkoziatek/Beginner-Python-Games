#_______________________________ Main Minesweeper Game Function _______________________________
#This function can be done in command prompt.
#You need python downloaded to use.
#To play, change your commmand prompt directly to where ever this folder is.
#Type: "python main.py" to start game. This may be different wording for your computer/python software.

import time
import sys
import random

# ________________ Create Minesweeper Class with inside Funtions ________________
class Minesweeper():

    # ________________ Create Minesweeper Board Generator Funtion ________________
    def generator(b_dim):
        #create empty list of bomb locations to add to later
        bomb_locations = []
        #make the number of bombs equal to the board side size
        bombs = b_dim
        #Create a list for rows
        rows = []

        #Create locations for bombs
        while len(bomb_locations) < bombs:
            #Create random locations for the bombs
            #The range is 0 to b_dim*b_dim-1.
            #row 0, column #0 is 0 | row 0, column 7 is 7
            # row dim-1, column dim-1 is #b_dim*b_dim-1
            random_number = random.randint(0,b_dim*b_dim-1)

            #if location was already picked for a bomb, don't add it to list
            if not (random_number in bomb_locations):
                bomb_locations.append(random_number)

        #Sort the list for easy shifting through.
        bomb_locations = sorted(list(bomb_locations))

        #create board with 0's and then fill with bombs
        while len(rows) < (b_dim):
            x = len(rows)
            rows.append([])
            while len(rows[x]) < (b_dim):
                rows[x].append(0)


        #Add numbers to board to show how many bombs are near it
        #The bombs will be inserted after the numbers are created
        for i in range(len(bomb_locations)):
            #bomb index for i. To shorten lines
            b_i = bomb_locations[i]

            #Create variables and values for the row and column for bomb bomb_locations
            r = int(b_i / b_dim)
            c = b_i % b_dim

            # _________ Current Row _________
            #Add one to the numbers above and to the left&right of bomb
            #Left
            if not (c == 0):
                rows[r][c - 1] = rows[r][c - 1] + 1
            #Right
            if c < (b_dim - 1):
                rows[r][c + 1] = rows[r][c + 1] + 1
            #_________Row Above _________
            #Add one to the number stored above the bomb if it's not the top row
            #Add one to the numbers above and to the left&right of it
            if not (r == 0):
                rows[r - 1][c] = rows[r - 1][c] + 1
                #Add one to the number above and to the left of bomb. If not on edge.
                #Row above and Left
                if not (c == 0):
                    rows[r - 1][c - 1] = rows[r - 1][c - 1] + 1
                #Add one to the number above and to the right of bomb. If not on edge.
                #Row above and Right
                if c < (b_dim - 1):
                    rows[r - 1][c + 1] = rows[r - 1][c + 1] + 1
            #_________Row Below _________
            #Add one to the numbers below the bomb if not on edge of Board
            if r < (b_dim - 1):
                rows[r + 1][c] = rows[r + 1][c] + 1
                #Below and to Left
                if not (c == 0):
                    rows[r + 1][c - 1] = rows[r + 1][c - 1] + 1
                #Below and to Right
                if c < (b_dim - 1):
                    rows[r + 1][c + 1] = rows[r + 1][c + 1] + 1

        #Add bombs to board
        # * Illustrates that it's a bomb
        for i in range(len(bomb_locations)):
            #Create variables and values for the row and column for bomb bomb_locations
            r = int(bomb_locations[i] / b_dim)
            c = bomb_locations[i] % b_dim
            rows[r][c] = '*'

        return rows;

    # ________________________________  Dig Funtion. Updates the visiable board ________________________________
    def dig(rows,visiable_board,b_dim,r,c):
        game_end = False

        #check if the dig location has a bomb

        if rows[r][c]=="*":
            game_end = True
            print("Baaam!! You found a mine! You lost.")
        #check if the dig location is a location with a bomb near it
        #if so, just put the number.
        elif rows[r][c] in range(1,5):
            visiable_board[r][c] = rows[r][c]
        #Check if the dig location doesnt have bombs near it
        #if so, find all the locations near it with no bombs and the 1st layer of numbers
        elif rows[r][c]==0:
            #create a list full of locations that were just digged
            #This is created to check around every area that is dug up
            dig_locations = [[r,c]]
            visiable_board[r][c] = rows[r][c]

            #while there is still locations to be searched around. Search em!
            while not (len(dig_locations)==0):
                dig_loc = dig_locations[0]
                r = dig_loc[0]
                c = dig_loc[1]

                #_______Above The Dig Site Check! ______
                #Check above sites to see if theres a 0 or a number
                #If it is, add to the board value to the visiable board
                if (r > 0 ):
                    if rows[r-1][c] == 0 and visiable_board[r-1][c]== " ":
                        #add the new open space to dig dig locations
                        dig_locations.append([r-1,c])
                    #Make the dug area visiable to user
                    visiable_board[r-1][c] = rows[r-1][c]

                    #____Diagonal left___
                    #if the bomb index divided by the board dimension size has no remainder,
                    #It's on the leftest column of the board
                    if c > 0:
                        if rows[r-1][c-1] == 0  and visiable_board[r-1][c-1]== " ":
                            #add the new open space to dig dig locations
                            dig_locations.append([r-1,c-1])
                            #Make the dug area visiable to user
                            visiable_board[r-1][c-1] = rows[r-1][c-1]

                    #____Diagonal right  ____
                    #if the bomb's index + 1 has no remainder, its on the right edge of board.
                    if c < (b_dim - 1):
                        if rows[r-1][c+1] == 0 and visiable_board[r-1][c+1]== " ":
                            #add the new open space to dig dig locations
                            dig_locations.append([r-1,c+1])
                        #Make the dug area visiable to user
                        visiable_board[r-1][c+1] = rows[r-1][c+1]

                #_______Horizontal To Dig Site Check! ______
                #To the left and right of the dig location to see if its 0 or a number
                #If it is, add to the board value to the visiable board
                #____ Left  ____
                if c > 0:
                    if rows[r][c-1] == 0 and visiable_board[r][c-1]== " ":
                        #add the new open space to dig dig locations
                        dig_locations.append([r,c-1])
                    #Make the dug area visiable to user
                    visiable_board[r][c-1] = rows[r][c-1]

                #____ Right  ____.
                if c < (b_dim - 1):
                    if rows[r][c+1] == 0 and visiable_board[r][c+1]== " ":
                        #add the new open space to dig dig locations
                        dig_locations.append([r,c+1])
                    #Make the dug area visiable to user
                    visiable_board[r][c+1] = rows[r][c+1]

                #_______Below The Dig Site Check! ______
                #Check above sites to see if theres a 0 or a number
                #If it is, add to the board value to the visiable board
                if r < (b_dim-1):
                    if rows[r+1][c] == 0 and visiable_board[r+1][c]== " ":
                        #add the new open space to dig dig locations
                        dig_locations.append([r+1,c])
                    #Make the dug area visiable to user
                    visiable_board[r+1][c] = rows[r+1][c]

                    #____Diagonal Down left___
                    if c>0:
                        if rows[r+1][c-1] == 0 and visiable_board[r+1][c-1]== " ":
                            #add the new open space to dig dig locations
                            dig_locations.append([r+1,c-1])
                        #Make the dug area visiable to user
                        visiable_board[r+1][c-1] = rows[r+1][c-1]

                    #____Diagonal Down right  ____
                    if c<(b_dim-1):
                        if rows[r+1][c+1] == 0 and visiable_board[r+1][c+1]== " ":
                            #add the new open space to dig dig locations
                            dig_locations.append([r+1,c+1])
                        #Make the dug area visiable to user
                        visiable_board[r+1][c+1] = rows[r+1][c+1]

                dig_locations.remove(dig_loc)

        return visiable_board,game_end

    # ________________________________  print_board Funtion ________________________________
    def print_board(rows, b_dim):

        #Create column header and divider
        column_header = "   "
        divider = "---"
        i = 0
        while i < b_dim :
            column_header = column_header + str(i) + "   "
            divider = divider + "----"
            i = i + 1


        print(f"{column_header}")
        print(f"{divider}")

        #A while loop to create the rows as a string and print them
        r = 0
        while r < b_dim:
            #create while loop to create columns in rows
            c = 0
            row_print = str(r) + " "
            while c < b_dim:
                row_print = row_print + "|" + str(rows[r][c]) + "  "
                c = c + 1

            print(f"{row_print}")
            r = r + 1





def main(b_dim = 10):
    play_again = 'Y'

    while play_again == 'Y':
        game_end = False
        #Introduce the player to the game!
        print("Welcome to python Minesweeper!")
        print("To win you need to dig up all the spaces that don't have a bomb.")
        print("If you pick a location that has a bomb you lose.")
        print("If a location has a 0. There are no bombs touching that space. Even diagonally.")
        print("If a location has a 1 or higher. That location is touching that number of bombs.")

        b_dim = int(input("How many rows do you want the board to be? Range is 2-25: "))
        if not b_dim in range(2, 25):
            b_dim = 8

        #call minesweeper_generator funtion to create a new minesweeper board
        board = Minesweeper.generator(b_dim)

        #create an empty board that gets filled with seen areas for user.
        visiable_board = []
        while len(visiable_board) < (b_dim):
            x = len(visiable_board)
            visiable_board.append([])
            while len(visiable_board[x]) < (b_dim):
                visiable_board[x].append(" ")


        #While the user is still palying the game and hasn't lost. continue
        while game_end == False:

            #Show the player the board
            print("Your current board:")
            Minesweeper.print_board(visiable_board,b_dim)

            #save the coordinates the player input and calculate the list's index
            r,c = input("Enter the location you would like to dig. As 'row,column': ").split(",",2)
            r = int(r)
            c = int(c)

            #Determine if the dig location was opened already
            if visiable_board[r][c] ==" ":
                visiable_board,game_end = Minesweeper.dig(board,visiable_board, b_dim, r,c)
            else:
                print("The location you picked was already known. Try again.")

            #Calculate if there are any spots left for the player to play.
            sum = 0
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if not board[i][j] == "*":
                        if visiable_board[i][j] == " ":
                            sum = sum + 1
            #If they've dug all the spaces besides the bombs, they won
            if sum == 0:
                game_end = True
                print("Great Job!! You won!")

        #Show the player the full board
        print("The board:")
        Minesweeper.print_board(board,b_dim)
        #Ask the player if they'd like to play again
        play_again = input("Would you like to play again? Y/N: ").upper()









main(8)
