# _______________________________ AI Function for the computer to strategically pick its space _______________________________

#import random function to keep it differce
import random

def computer_ai_choice(b, b_open):
    #diagram of board_open
    # 1 | 2 | 3
    # ---------
    # 4 | 5 | 6
    # ---------
    # 7 | 8 | 9
        # b[0] | b[1] | b[2]
        # ------------------
        # b[3] | b[4] | b[5]
        # ------------------
        # b[6] | b[7] | b[8]

    #Since the computer goes 2nd, the best strategy is to pick the middle place first
    #If the player didn't take it and took a corner.
    #(b[0]=='X' or b[2]=='X' or b[6]=='X' or b[8]=='X'):
    if 5 in b_open:
        choice = 5

    #pick the 3rd space that the computer needs to take to win
    #First row options
    elif (b[1]=='O' and b[2]=='O') and (1 in b_open):
        choice = 1
    elif (b[0]=='O' and b[2]=='O') and (2 in b_open):
        choice = 2
    elif (b[0]=='O' and b[1]=='O') and (3 in b_open):
        choice = 3
    #Second row options
    elif (b[4]=='O' and b[5]=='O') and (4 in b_open):
        choice = 4
    elif (b[3]=='O' and b[5]=='O') and (5 in b_open):
        choice = 5
    elif (b[3]=='O' and b[4]=='O') and (6 in b_open):
        choice = 6
    #Third row options
    elif (b[7]=='O' and b[8]=='O') and (7 in b_open):
        choice = 7
    elif (b[6]=='O' and b[8]=='O') and (8 in b_open):
        choice = 8
    elif (b[6]=='O' and b[7]=='O') and (9 in b_open):
        choice = 9
    #First column options
    elif (b[3]=='O' and b[6]=='O') and (1 in b_open):
        choice = 1
    elif (b[0]=='O' and b[6]=='O') and (4 in b_open):
        choice = 4
    elif (b[0]=='O' and b[3]=='O') and (7 in b_open):
        choice = 7
    #Second column options
    elif (b[4]=='O' and b[7]=='O') and (2 in b_open):
        choice = 2
    elif (b[1]=='O' and b[7]=='O') and (5 in b_open):
        choice = 5
    elif (b[1]=='O' and b[4]=='O') and (8 in b_open):
        choice = 8
    #Third column options
    elif (b[5]=='O' and b[8]=='O') and (3 in b_open):
        choice = 3
    elif (b[2]=='O' and b[8]=='O') and (6 in b_open):
        choice = 6
    elif (b[2]=='O' and b[5]=='O') and (9 in b_open):
        choice = 9
    #left diagnol options
    elif (b[4]=='O' and b[8]=='O') and (1 in b_open):
        choice = 1
    elif (b[0]=='O' and b[8]=='O') and (5 in b_open):
        choice = 5
    elif (b[0]=='O' and b[4]=='O') and (9 in b_open):
        choice = 9
    #Right diagnol options
    elif (b[4]=='O' and b[6]=='O') and (3 in b_open):
        choice = 3
    elif (b[2]=='O' and b[6]=='O') and (5 in b_open):
        choice = 5
    elif (b[2]=='O' and b[4]=='O') and (7 in b_open):
        choice = 7

    #pick the 3rd space that the player needs, so they don't win
    #First row options
    elif (b[1]=='X' and b[2]=='X') and (1 in b_open):
        choice = 1
    elif (b[0]=='X' and b[2]=='X') and (2 in b_open):
        choice = 2
    elif (b[0]=='X' and b[1]=='X') and (3 in b_open):
        choice = 3
    #Second row options
    elif (b[4]=='X' and b[5]=='X') and (4 in b_open):
        choice = 4
    elif (b[3]=='X' and b[5]=='X') and (5 in b_open):
        choice = 5
    elif (b[3]=='X' and b[4]=='X') and (6 in b_open):
        choice = 6
    #Third row options
    elif (b[7]=='X' and b[8]=='X') and (7 in b_open):
        choice = 7
    elif (b[6]=='X' and b[8]=='X') and (8 in b_open):
        choice = 8
    elif (b[6]=='X' and b[7]=='X') and (9 in b_open):
        choice = 9
    #First column options
    elif (b[3]=='X' and b[6]=='X') and (1 in b_open):
        choice = 1
    elif (b[0]=='X' and b[6]=='X') and (4 in b_open):
        choice = 4
    elif (b[0]=='X' and b[3]=='X') and (7 in b_open):
        choice = 7
    #Second column options
    elif (b[4]=='X' and b[7]=='X') and (2 in b_open):
        choice = 2
    elif (b[1]=='X' and b[7]=='X') and (5 in b_open):
        choice = 5
    elif (b[1]=='X' and b[4]=='X') and (8 in b_open):
        choice = 8
    #Third column options
    elif (b[5]=='X' and b[8]=='X') and (3 in b_open):
        choice = 3
    elif (b[2]=='X' and b[8]=='X') and (6 in b_open):
        choice = 6
    elif (b[2]=='X' and b[5]=='X') and (9 in b_open):
        choice = 9
    #left diagnol options
    elif (b[4]=='X' and b[8]=='X') and (1 in b_open):
        choice = 1
    elif (b[0]=='X' and b[8]=='X' and (5 in b_open)):
        choice = 5
    elif (b[0]=='X' and b[4]=='X') and (9 in b_open):
        choice = 9
    #Right diagnol options
    elif (b[4]=='X' and b[6]=='X') and (3 in b_open):
        choice = 3
    elif (b[2]=='X' and b[6]=='X') and (5 in b_open):
        choice = 5
    elif (b[2]=='X' and b[4]=='X') and (7 in b_open):
        choice = 7

    #pick any a random corner if none of the edge spaces are taken
    elif (1 and 2 and 3 and 4 and 6 and 7 and 8 and 9) in b_open:
        choice = random.choice([1,3,7,9])
    #choice a corner opposite if any it has
    elif (b[0]=='O' and ((3 and 7 and 9) in b_open)):
        choice = 9
    elif (b[2]=='O' and ((1 and 7 and 9) in b_open)):
        choice = 7
    elif (b[6]=='O' and ((1 and 3 and 9) in b_open)):
        choice = 3
    elif (b[8]=='O' and ((1 and 3 and 7) in b_open)):
        choice = 1

    #Pick another space to get closer to 3!
    #When the computer has spaces 1 and 9.
    elif (b[0]=='O' and b[8]=='O') and ((3 and 7) in b_open):
        if (2 and 3 and 6 and 4 and 7 and 8) in b_open:
            choice = random.choice([3,7])
        elif (2 and 3 and 6) in b_open:
            choice = 3
        elif (4 and 7 and 8) in b_open:
            choice = 7
        else:
            choice = random.choice([3,7])
    #When the computer has spaces 3 and 7.
    elif (b[2]=='O' and b[6]=='O') and ((1 and 9) in b_open):
        if (1 and 2 and 4 and 6 and 8 and 9) in b_open:
            choice = random.choice([1,9])
        elif (1 and 2 and 4) in b_open:
            choice = 1
        elif (6 and 8 and 9) in b_open:
            choice = 9
        else:
            choice = random.choice([1,9])
    else:
        choice = random.choice(b_open)
    return choice
