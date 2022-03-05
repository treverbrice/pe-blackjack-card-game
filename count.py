import hand

class count(hand.hand):
    def __init__(self, *args):
        self.count = 0
        self.cards = []
        self.addCard(*args)

    def addCard(self, *new_cards):
        for card in new_cards:
            if card.getValue() <= 6:
                self.count += 1
            elif card.getValue() >= 10:
                self.count -= 1
            self.cards.append(card)

    def numCards(self):
        return len(self.cards)
