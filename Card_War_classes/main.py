#_______________________________ War Card Game Main _______________________________
#This function can be done in command prompt.
#You need python downloaded to use.
#To play, change your commmand prompt directly to where ever this folder is.
#Type: "python main.py" to start game. This may be different wording for your computer/python software.

#This python file creates a deck of 52 card of the 4 suits
#It divides the cards up randomly between the player and the computer
#The rules of the card game War apply here
#1: Both the computer and the player flip over their top card.
#   who ever's rank is higher takes the cards
#2: If the cards are the same rank. Its a battle!
#   The player and the computer turn up one card face down and one card face up.
#   Who ever has the higher card takes both piles (six cards)
#   If they're the same, battle again!

import random
from deck import Deck
from card import Card

# ____________ Play War Function ____________
def play():
    #initialize playing variables
    play_again = 'Y'
    while play_again == 'Y':
        game_over = False

        #Create and shuffle the deck of cards
        d = Deck()
        d.create_deck()
        d.shuffle()
        d.shuffle()

        #create deck for player
        p_deck = []
        for i in range(26):
            p_deck.append(d.deck_of_cards.pop(0))

        #create deck for computer
        c_deck = []
        for i in range(26):
            c_deck.append(d.deck_of_cards.pop(0))

        #Create variables to store that amount of cards each player won
        p_total = 0
        c_total = 0

        #Welcome player!
        print("Welcome to the game of war! A game of luck.")
        print("This game is between you and the computer.")
        print("You both have a split deck of cards (26 each).")
        print("Each round one of your cards are flipped.")
        print("Whoever's card has a higher rank card takes all the cards.")
        print("If you draw the same rank, it's a war!")
        print("You both flip over two cards, the 2nd is compared to find a winner.")
        print("If those cards have the same rank you flip again.")
        print("If there's not enough cards, you just flip the 1st card or draw.")
        print("Whoever has the most cards when the decks run out wins.")
        cont1 = input("Press Enter to contiue! ")

        #While loop while decks still have cards
        while game_over == False:

            #Draw cards for the player and the computer
            p_card = p_deck.pop(0)
            c_card = c_deck.pop(0)
            print(f"\t You drew: {p_card.get_string_rank()} of {p_card.suit}.")
            print(f"\t Computer drew: {c_card.get_string_rank()} of {c_card.suit}.")

            #compare the Cards
            p_deck,c_deck,p_total,c_total = compare_cards(p_card,c_card,p_deck,c_deck,p_total,c_total,2)

            print(f"Total Score (You/Comp): {p_total} / {c_total}")
            #If the decks are empty, end game
            if len(p_deck) == 0:
                game_over = True
                print("The decks are empty. Game over.")
            #Else, Allow the player to continue
            else:
                cont = input("Press N to stop playing. Any other to continue: ").upper()
                if cont == 'N':
                    game_over = True

        #Tell player the results!
        print(f"You have {p_total} cards. The computer has {c_total} cards.")
        if p_total > c_total:
            print("You won this game!")
        elif p_total < c_total:
            print("You lost this game.")
        else:
            print("It's a tie this game!")


        play_again = input("Would you like to play again? Type Y if so: ").upper()

# ____________ Compare Cards Function ____________
def compare_cards(p_card,c_card,p_deck,c_deck,p_total,c_total,win_cards):

    if p_card.rank>c_card.rank:
        print("You won!")
        p_total += win_cards
    elif p_card.rank<c_card.rank:
        print("You lost.")
        c_total += win_cards
    #You have the same rank. It's war!
    else:
        if len(p_deck) > 0:
            p_deck,c_deck,p_total,c_total = war(p_deck,c_deck,p_total,c_total,win_cards)

    return p_deck,c_deck,p_total,c_total


# ____________ War Function ____________
def war(p_deck,c_deck,p_total,c_total, win_cards):
    print("You both drew the same rank! It's war!")
    print("You both are drawing 2 cards, and flipping the 2nd to compare.")

    #Remove one card and flip the 2nd
    if len(p_deck) > 1:
        p_deck.pop(0)
        c_deck.pop(0)
        win_cards += 4
    else:
        print("There are not enough cards in deck. Only checking the 1 card in war now.")
        win_cards += 2
    p_card = p_deck.pop(0)
    c_card = c_deck.pop(0)

    print(f"\t You drew: {p_card.get_string_rank()} of {p_card.suit}.")
    print(f"\t Computer drew: {c_card.get_string_rank()} of {c_card.suit}.")

    if p_card.rank > c_card.rank:
        p_total += win_cards
        print("You won this round!")
    elif p_card.rank < c_card.rank:
        c_total += win_cards
        print("You lost this round")
    else:
        if len(p_deck) > 0:
            print("It's a tie this round! War again!")
            p_deck,c_deck,p_total,c_total = war(p_deck,c_deck,p_total,c_total,win_cards)
        else:
            print("It's a draw. Not enough cards in deck left.")


    return p_deck,c_deck,p_total,c_total



# ____________ Initialization tasks ____________
if __name__ == '__main__':
    play()
