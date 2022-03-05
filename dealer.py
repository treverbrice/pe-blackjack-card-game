# dealer gets its first two cards in opening()
# dealer plays its hand with a method
# has a method for checking for a natural, used if player gets a natural

from hand import hand
import time

class dealer:
    def __init__(self):
        pass


    def opening(self, deck):
        card_one = deck.deal()
        card_two = deck.deal()

        print(f"The dealer is dealt: {card_one}")
        time.sleep(1)
        print(f"The dealer is dealt: Unkown")
        time.sleep(1)

        self.hand = hand(card_one, card_two)

        return


    def playRound(self, deck):
        print(f"The dealer has: {self.hand}")
        time.sleep(1)

        while self.hand.getValue() <= 16:
            new_card = deck.deal()
            print(f"The dealer is dealt: {new_card}")
            time.sleep(1)

            self.hand.addCard(new_card)
            print(f"The dealer has: {self.hand}")
            time.sleep(1)

        print("The dealer stays")
        return


    def checkNatural(self):
        print(f"The dealer has: {self.hand}")
        time.sleep(1)
        return(self.hand.getValue() == 21)


    def getValue(self):
        return self.hand.getValue()
