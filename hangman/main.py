# ************************************* Hangman Game! *************************************
#This game is played on command prompt.
#You need python downloaded to use.
#To play, change your commmand prompt directly to where ever this folder is.
#Type: "python main.py" to start game. This may be different wording for your computer/python software.

#import random function and list of words from directory and words.py
#words.py is a python file that holds a list of words in a list.
import random
import string
from words import words


#Create function to find and create valid word for hangman thats all UPPERCASE
# the word file may have spaces and -. This function finds words without them.
def get_valid_word(words):
    #find random word and make it uppercase.
    computer_word_choice = random.choice(words).upper()
    #find new word when it contains " " or "-"
    while (" " in computer_word_choice) or ("-" in computer_word_choice):
        computer_word_choice = random.choice(words).upper()

    #return the word
    return computer_word_choice



#Create hangman function

def hangman():
    #create variable that restarts hangman game if player desires.
    play_again = "Y"
    #create whileloop for when user is playing.
    #Ends when player doesn't type "Y" at the end of game.
    while play_again == "Y":
        #Get valid word from get_valid_word function.
        #this includes no spaces or -
        word = get_valid_word(words)
        #put all letters into set (a list of letters that has no repeats).
        #This is used to show how many letters the user has left to guess.
        word_letters = set(word)
        #create variable with all letters in the alphabet.
        #This is used to see what letters the user has left to guessed
        alphabet = set(string.ascii_uppercase)
        #Create set that will contain all the letters guessed by user
        used_letters = set()
        #set the lives of the hanged man, aka his limbs
        lives=6

        #Create while loop for when user's has more letters in the word to guess and more tries/lives
        while len(word_letters) >0 and lives>0:
            #Create word_list with all the letters the user got right and their locations.
            #User "-" as a placholder for all letters they haven't guessed yet.
            word_list= [letter if letter in used_letters else "-" for letter in word]
            #Tell the user the number of characters in the word and letters they've guessed right.
            #Tell the user all the letters they've Guessed
            #Tell the user the amount of lives (aka wrong guesses) they have left.
            #''.join([1,2,3,4]) - > '1 2 3 4'
            print("Current word: " , " ".join(word_list) , " | " , "Guessed Letters: " , " ".join(used_letters) , " | " , f"Lives left: {lives}")
            #Prompt the user to input a letter to guess. Uppercase it to keep uniform.
            user_guess = input("Guess a letter: "). upper()

            #If Statement to shift through the possible outcomes of what the user input
            #If the user's guess is in the alphabet and wasn't already guessed, continue.
            if user_guess in alphabet-used_letters:
                #Add user's guess to the used_letters variable to keep track.
                used_letters.add(user_guess)
                #If user's guess is in the word, remove it from the word_letters left to guess list.
                if user_guess in word_letters:
                    #decrease the word_letters letter that is used_letters
                    word_letters.remove(user_guess)
                #If user's guess was not in the word, remove one life/wrong guess from Lives variable.
                else:
                    lives = lives-1
                    #print(f"You got it wrong. You have {lives} tries left now.")
            #If user's guess was already guessed. let the know.
            elif user_guess in used_letters:
                print("You have guessed that letter already. No lives were taken.")
            #If else, the user's guess was not in the alphabet.
            else:
                print("You have typed an invalid character.")

        #This part of the function is outside the play current word loop.
        #If the word_letters list if empty it means that the user guessed all the letters in the words
        if len(word_letters)==0:
            print(f"You guessed the word! It was {word}!")
        #If the lives is 0. The user has no more tries and the game ends.
        elif lives==0:
            print(f"You ran out of guesses. It was {word}!")
        #Prompt the user to play again. "Y" or "y" to play again. Anything else it ends.
        play_again = input("Would you like to play again? Y/N: ").upper()

#Call the hangman function to play!
hangman()
