import deck as d


class player:
    def __init__(self):
        self._cards_to_have = 13
        self._hand = []
        self.turn = False
        self.bet = 0
        self.

    def init_hand(self,new_cards):
        self._hand = new_cards

    def play_card(self,choice):
        pass

class game:
    def __init__(self) -> None:
        self._num_players = 4
        self._players = {}
        for i in range(self._players):
            self._players['P{}'.format(i)] = player()
        self._deck = d.deck(41)
        self._scores = {'P0' : 0, 'P1':  0, 'P2': 0, 'P3': 0}
        self._teams_1 = ['P0', 'P2']
        self._teams_2 = ['P1','P3']
        self._team_1_passed = False
        self._team_2_passed = False
        self._tarneeb = 'S'
        

        
    def game_ended(self):
        # TODO: Check what happens if both teams passed the 41 threshhold
        if self._team_1_passed:
            if self._team_2_passed:
                return False
            else:
                return True
        if self._team_2_passed:
            return True
        
        return False

    def evaluate_score(self):
        if (self._scores[self._team_1[0]] +  self._scores[self._team_1[1]]) >= 41:
            self._team_1_passed = True
        
        if (self._scores[self._team_2[0]] +  self._scores[self._team_2[1]]) >= 41:
            self._team_2_passed = True

    def distribute_cards(self):
        
        self._players[]

    def print_scores(self):
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
        self._deck.shuffel_deck()
        self.distribute_cards()
        self.evaluate_score()
        self.print_scores()




if __name__ == '__main__':
    g = game()
    while(g.game_ended()):
        g.play_round()
        
