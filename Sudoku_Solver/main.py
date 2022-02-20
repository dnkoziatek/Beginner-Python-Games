#_______________________________ Sudoku Puzzle Solver _______________________________
#This function can be done in command prompt.
#You need python downloaded to use.
#To play, change your commmand prompt directly to where ever this folder is.
#Type: "python main.py" to start game. This may be different wording for your computer/python software.

import random
from puzzles import puzzles


#For visual aid. Below is the nested list of puzzle with rows and columns
#   puzzle[row][column]
#     0|1|2|3|4|5|6|7|8|
#   0| | | | | | | | | |
#   1| | | | | | | | | |
#   2| | | | | | | | | |
#   3| | | | | | | | | |
#   4| | | | | | | | | |
#   5| | | | | | | | | |
#   6| | | | | | | | | |
#   7| | | | | | | | | |
#   8| | | | | | | | | |




# ________________ Solve Sudoku Function ________________
#main function that calls all other functions to solve the sudoku puzzle
#Returns True,puzzle for a solvable/completed puzzle
#Returns False,puzzle for unsolvalbe puzzle
def solve_sudoku(puzzle):

    #choose the next open location for the puzzle
    # 0 was set as empty locations for ease of use
    # The only valid numbers are 1-9
    #The function returns None,None if no spaces are left
    r,c = next_empty_location(puzzle)

    #The function returns None,None if no spaces are left
    #If no spaces are left, return True because it was solvable and the puzzle
    if r==None and c==None:
        return True,puzzle


    #Try numbers 1 to 9 in the location of r,c
    for i in range(1,10):
        #If guess i is valid, try the entire puzzle with i
        if is_valid(puzzle, i, r, c):
            puzzle[r][c] = i
            #If puzzle was solved the puzzle is valid
            valid,puzzle = solve_sudoku(puzzle)
            if valid:
                return True,puzzle

        #if the guess did not create a valid completable puzzle
        #Try the next number in the Range
        puzzle[r][c] = 0


    #If no range of numbers 1 - 9 returned a True completable puzzle
    #The puzzle is unsolvalbe
    return False,puzzle



# ________________ Next Empty Location of the Puzzle Function ________________
#function find the next empty (=0) location in the puzzle
#The return is row,column
#If there is no empty locations. Return None,None
def next_empty_location(puzzle):
    #check all rows and columns of puzzle
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r,c

    return None,None



#***** test print is in here *******
# ________________ Is Valid Function ________________
#function to check if guess is valid for  the puzzle
#Returns True if the guess is valid in the puzzle location
def is_valid(puzzle, guess, row, column):

    #Check the row for #1-9
    #if the guess is in the row, it's not valid
    if guess in puzzle[row]:
        return False
    #Check the column for #1-9
    #if the guess is in the column, it's not valud
    for i in range(9):
        if guess == puzzle[i][column]:
            return False

    #Check cube for #1-9
    #if the guess is in the cube, it's not Valid
    #Calculate the starting rows and columns to easily
    #find the section it's in
    cube_start_row = (row//3) * 3
    cube_start_column = (column//3) * 3
    # Search through the 3x3 cube to see if the guess is in it
    for r in range(cube_start_row, cube_start_row + 3):
        for c in range(cube_start_column, cube_start_column + 3):
            if guess == puzzle[r][c]:
                return False

    #return true if it didn't find the guess anywhere
    return True



# ________________ Print Puzzle Function ________________
#function that prints puzzle to command prompt neatly
#No return
def print_puzzle(puzzle):
    dim = 9

    #Create column header and divider
    column_header = "   "
    divider = "---"
    i = 0
    while i < dim :
        column_header = column_header + str(i) + "   "
        divider = divider + "----"
        i = i + 1

    print(f"{column_header}")
    print(f"{divider}")

    #A while loop to create the rows as a string and print them
    r = 0
    while r < dim:
        #create while loop to create columns in rows
        c = 0
        row_print = str(r) + " "
        while c < dim:
            row_print = row_print + "|" + str(puzzle[r][c]) + "  "
            c = c + 1

        print(f"{row_print}")
        r = r + 1



#If this python file is the main function being called
#This acts as a constructor to start the code
if __name__ == '__main__':
    #Pick a random empty puzzle from the puzzle.py list of puzzles
    puzzle = puzzles[random.randint(0,len(puzzles) - 1)]

    #print empty puzzles
    print_puzzle(puzzle)
    #print solved puzzle
    valid,puzzle_done = solve_sudoku(puzzle)
    print(f"Puzzle valid?: {valid}")
    print(f"Solved sudoku board: ")
    if valid == True:
        print_puzzle(puzzle_done)
