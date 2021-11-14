import pytest
import deck as d
import copy

n_deck = d.deck(41)

def test_deck_shuffel():
    n1_cards = copy.deepcopy(n_deck.show_deck())
    n_deck.shuffel_deck()
    n2_cards = n_deck.show_deck()
    res = list(map(lambda n1, n2: n1 == n2, n1_cards, n2_cards))
    assert False in res, "test failed: deck was not shuffeled"
    for i in range(len(n2_cards)):
        for j in range(len(n2_cards)):
            if i == j:
                continue
            assert not n2_cards[i] == n2_cards[j], "test failed: deck contains duplicates"

if __name__ == "__main__":
    test_deck_shuffel()

