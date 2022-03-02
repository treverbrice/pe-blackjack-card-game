# deck class has shuffle and deal methods

from card import card
import random

class deck:

    def __init__(self):
        self.cards = []
        suits = ["spade", "club", "heart", "diamond"]
        for suit in range(4):
            ace = card(suits[suit], "a")
            self.cards.append(ace)

            for num in range(2, 11):
                new_card = card(suits[suit], num)
                self.cards.append(new_card)

            jack = card(suits[suit], "j")
            queen = card(suits[suit], "q")
            king = card(suits[suit], "k")
            self.cards.append(jack)
            self.cards.append(queen)
            self.cards.append(king)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        top_card = self.cards.pop(0)
        return top_card
