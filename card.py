# card class, has suit, and value
# toStr method, get string of suit and value
# getValue method, should be easily callable and return 10 = K,Q,J 11 = A
# spade = u"\u2660" heart = u"\u2665" diamond = u"\u2666" club = u"\u2663"

class card:
    def __init__(self, suit, value):
        if suit.lower() == 'spade':
            self.suit = u"\u2660"
        elif suit.lower() == 'heart':
            self.suit = u"\u2665"
        elif suit.lower() == 'diamond':
            self.suit = u"\u2666"
        elif suit.lower() == 'club':
            self.suit = u"\u2663"
        else:
            raise ValueError("invalid suit")
        self.value = str(value)

    def getValue(self):
        if self.value.isdigit():
            return int(self.value)
        elif self.value.lower() == 'a':
            return 11
        else:
            return 10

    def __repr__(self):
        return(self.suit + self.value)
