import Deck as d

'''
TODO: Documentation!!
'''

class player:
    def __init__(self, number):
        self._player_number = number
        self._cards_max = 13
        self._cards_to_have = self._cards_max
        self._hand = []
        self.turn = False
        self.bet = 0
        

    def init_hand(self,new_cards):
        self._hand = new_cards

    def give_card(self, card):
        if self._cards_to_have > 0:
            self._hand.append(card)
            return 0
        else:
            return -1
        

    def play_card(self,choice):
        pass

class game:
    def __init__(self) -> None:
        
        self._num_players = 4
        
        # Initialize players
        self._players = {}
        for i in range(self._players):
            self._players['P{}'.format(i)] = player(i)
        
        # Initialize deck
        self._deck = d.Deck("tarneeb_41")

        # Initialize scores
        self._scores = {'P0' : 0, 'P1':  0, 'P2': 0, 'P3': 0}

        # Which player is in which team
        self._teams_1 = ['P0', 'P2']
        self._teams_2 = ['P1','P3']

        # When a team passes the 41 Threshhold, it's variable will become true
        self._team_1_passed = False
        self._team_2_passed = False

        # only becomes true if both teams passed threshold. 
        self._draw_turn = False
        
        
        """
        Call this function to check wether a game has ended. A Game ends when a Player in a Team has 41 points 
        or more and the second player has a positive score (The >=(41,0) Threshhold). The Team which meets this rule wins. 


        If both players finished a turn, where both teams has a player with score >= 41 and another player >= 0, 
        one last turn will be played and the team with the highest score wins. 
        """
    def game_ended(self):

        if self._draw_turn:
            return False
        
        if self._team_1_passed:
            if self._team_2_passed:
                return False
            else:
                return True
        if self._team_2_passed:
            return True
        
        return False

    """
    Checks whether a team passed the >=(41,0) threshhold
    """
    def evaluate_score(self):

        if (self._scores[self._team_1[0]] +  self._scores[self._team_1[1]]) >= 41:
            self._team_1_passed = True
        
        if (self._scores[self._team_2[0]] +  self._scores[self._team_2[1]]) >= 41:
            self._team_2_passed = True
        
        # Both teams passed the >=(41,0) threshhold
        if self._team_1_passed and self._team_2_passed:
            self._draw_turn = True

    def distribute_cards(self,shuffels=10,distribution_pattern = 3):
        #TODO: Write a test
        if distribution_pattern == 3:
            id_player = 0
            counter = 0
            for i in range(16):
                for card in self._cards:
                    if counter == 3:
                        break
                    counter = counter + 1
                    self._players['P{}'.format(id_player)].give_card(card)
                id_player = id_player + 1
            
            for i in range(4):
                self._players['P{}'.format(id_player)].give_card(self._cards[(-1)*i])
                

    def print_scores(self):

        #TODO: This needs to get updated because of self._draw_turn
        print("Scores: ")
        print("player 1 has {}".format(self._scores[self._team_1[0]]))
        print("player 3 has {}".format(self._scores[self._team_1[1]]))
        print("player 2 has {}".format(self._scores[self._team_2[0]]))
        print("player 4 has {}".format(self._scores[self._team_2[1]]))
        print("Player  1 and 3 are a team")
        print("Player  2 and 4 are a team")
        if self._team_1_passed:
            if self._team_2_passed:
                print("Both teams  are  ahead!")
            else:
                print("TEAM 1 WON!!!")
        if self._team_2_passed:
            print("TEAM 2 WON!!!")

        if not self.game_ended():
            print("Game did not end.")

    def play_round(self):
        tarneeb = 'S'
        last_cards = []
        self._deck.shuffel_deck()
        self.distribute_cards()
        self.evaluate_score()
        self.print_scores()


if __name__ == '__main__':
    g = game()
    while(g.game_ended()):
        g.play_round()
        
