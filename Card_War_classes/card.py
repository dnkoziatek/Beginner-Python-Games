#_______________________________ Card Class  _______________________________
#This file contains the class Card in which the details for a card are created and read
#
#To play you need to go to the Main.py file


class Card:
    #Create placeholder variables to be created
    rank = 0
    suit = ""

    def __init__(self,rank, suit):
        self.rank=rank
        self.suit=suit

    #Create function for simple card
    def card(self,rank, suit):
        rank = self.rank
        suit = self.suit

    def card(self,card):
        rank = card.rank
        suit = card.suit



    def get_string_rank(self):
        rank = self.rank
        if rank == 14:
            return "Ace"
        elif rank == 11:
            return "Jack"
        elif rank == 12:
            return "Queen"
        elif rank == 13:
            return "King"
        else:
            return str(rank)


#--------****temp ****
if __name__ == '__main__':
    c = Card(14, "Hearts")
    print(f"{c.get_string_rank()},{c.suit}")
