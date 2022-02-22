#_______________________________ Deck Class  _______________________________
#This file contains the class Deck in which the details for a card are created and read
#Deck is used to create, read, shuffle 52 cards for the game Way
#To play you need to go to the Main.py file

import random
from card import Card

class Deck:

    def __init__(self):
        self.deck_of_cards = []


    # ____________ Create a Deck Function ____________
    # No jokers are in the deck to play war
    #This deck is in order, and not shuffled
    def create_deck(self):
        deck_of_cards = self.deck_of_cards
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        #For loop to add card to Deck
        # s is for the 4 suits of the Deck
        # r is the for 13 ranks of the deck: 2-10, jack, queen, king, ace
        s = 0
        while s < 4:
            r = 2
            while r < 15:
                temp_card = Card(r,suits[s])
                deck_of_cards.append(temp_card)
                r = r + 1
            s = s + 1

        for i in deck_of_cards:
            print(f"[{i.rank},{i.suit}]")

        return deck_of_cards


    # ____________ Shuffle Deck Function ____________
    def shuffle(self):
        deck_of_cards = self.deck_of_cards
        for i in range(0,len(deck_of_cards)):
            print(f"Current iteration: {i}")
            x = random.randint(0,len(deck_of_cards)-1)
            c = deck_of_cards[i]
            b = deck_of_cards[x]
            deck_of_cards[x] = c
            deck_of_cards[i] = b

    # ____________ Print Deck Function ____________
    def print_deck(self):
        deck_of_cards = self.deck_of_cards
        for i in deck_of_cards:
            print(f"[{i.get_string_rank()},{i.suit}] ")


if __name__ == '__main__':
    c = Card(11, "Hearts")
    print(f"{c.rank},{c.suit}")
    d = Deck()
    d.create_deck()
    d.print_deck()
    d.shuffle()
    d.shuffle()
    d.print_deck()

    #print(f"{d}")
