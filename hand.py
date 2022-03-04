# keeps track of what cards you have
# can return the value of the hand
# adjusts value for any aces
# can accept new cards

from card import card

class hand:
    def __init__(self, *args):
        self.cards = [*args]


    def getValue(self):
        num_aces = 0
        value = 0

        for card in self.cards:
            temp_value = card.getValue()
            if temp_value == 11:
                num_aces += 1
            value += temp_value

        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value


    def addCard(self, new_card):
        self.cards.append(new_card)


    def __repr__(self):
        return(str(self.cards))
