
import random

class card:

    """
        Initiate a card by choosing rank and suit. 
        Suit: either 'D' for Dimonds, 'C' for Clubs, 'H' for Hearts, 'S' for Spades
        rank: from 2 to 13, 2..10 for normal ranks, 11 for Jacks, 12 for Queens, 13 for Kings, 14 for Aces.
    """
    def __init__(self,suit,rank):
        self._rank = 2
        self._suit = 'D'
        if (suit == 'C') or suit == 'D' or suit == 'H' or suit == 'S':
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
    def get_content_string(self):
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

class deck:
    def __init__(self, game_type):
        if game_type == 41:
            self._cards = []
            self.initiate_41_deck()

    def initiate_41_deck(self):
        for suit in list(['C','S','H','D']):
            for i in range(2,15):
                self._cards.append(card(suit,i))

    def show_deck(self):
        return self._cards

    def number_of_cards(self):
        return len(self._cards)

    def cut_cards(self, number=20):
        if number > 0: 
            for i in range(number):
                self._cards.append(self._cards.pop(0)) 
    
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
    a = deck(41)
    for card in a.show_deck():
        print(card.get_content_string())
        
