
import random

from core import game

class card:

    """
        Initiate a card by choosing rank and suit. \
        Suit: either 'D' for Dimonds, 'C' for Clubs, 'H' for Hearts, 'S' for Spades \
        rank: from 2 to 13, 2..10 for normal ranks, 11 for Jacks, 12 for Queens, 13 for Kings, 14 for Aces.
    """
    def __init__(self,suit,rank):
        self._rank = 2
        self._suit = 'D'
        if (suit == 'C') or (suit == 'D') or (suit == 'H') or (suit == 'S'):
            self._suit = suit
        else:
            raise TypeError("Suit should be either C,D,H, or S.")
            
        if (rank < 2) or (rank > 14):
            raise ValueError("Rank should be from 2 to 14")
        else:
            self._rank = rank
    
    """
        Return suit and rank.
    """
    def get_content(self):
        return self._suit, self._rank

    """
    Returns suit and rank as string
    """
    def get_content_as_string(self):
        return "{0} {1}" .format(self._suit,self._rank)

    """
    Overloading '==' operator
    """
    def __eq__(self, card2):
        s, r = card2.get_content()
        if s == self._suit:
            if r == self._rank:
                return True
        return False

        

class Deck:

    """
    The deck class is responsible for preparing the correct deck structure and holds the playing cards. \
        The deck is also responsible for shuffeling and drawing. The initializer takes a String, which is for now \
            either "tarneeb_41" and "trex_long". "tarneeb_41" initializes the correct deck for the tarneb game with \
                the winning score of 41. "trex_long" prepares a deck for the Trex game with the 4 kingdoms, where every kingdom\
                    playes 5 different games. inputting anything else will result in an empty deck.
    """

    def __init__(self, game_type):
        self._cards = []

        #TODO: Check if you could change that to enum, does Enum exsit in Python ? 
        if game_type == "tarneeb_41":
            self._initiate_41_deck()
        elif game_type == "trex_long":
            self._initiate_trex_long_deck()
        else:
            print("initialized empty deck.")

    """
    Fills the deck with 52 cars, 13 of each kind. 
    """
    def _initiate_41_deck(self):
        for suit in list(['C','S','H','D']):
            for i in range(2,15):
                self._cards.append(card(suit,i))

    """
    Tarneeb and Trex have the same deck struckture. 
    """
    
    def _initiate_trex_long_deck(self):
        self._initiate_41_deck()
    
    def is_empty(self):
        if self._cards.count == 0:
            return True
        else:
            return False
        
    """
    Returns the deck itself.
    """
    def show_deck(self):
        return self._cards

    """
    Returns the number of cards.
    """
    def number_of_cards(self):
        return len(self._cards)

    """
    Cuts the cars in half at the specified position in 20. 
    """

    def cut_cards(self, number=20):
        if self.is_empty():
            if number > 0: 
                for i in range(number):
                    self._cards.append(self._cards.pop(0)) 
        else:
            print("nothing to cut")
    
    """
    Call this function to shuffel the deck. The shuffeling happens by calling cut_cards for a sepecified number of times.\
        This number can be given by specifing the shuffels parametes.
    """
    def shuffel_deck(self, shuffels = 5):
        
        
        deck_size = self.number_of_cards()
        for i in range(shuffels):
            n_index = random.randint(0,deck_size-1)
            self.cut_cards(n_index)

    def draw(self):
        return self._cards[0]
            
    def draw_last(self):
        return self._cards[-1]



if __name__ == '__main__':
    #TODO: Fix Here
    a = Deck("tarneeb_41")
    for card in a.show_deck():
        print(card.get_content_as_string())
        
