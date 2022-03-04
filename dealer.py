# dealer gets its first two cards in opening()
# dealer plays its hand with a method
# has a method for checking for a natural, used if player gets a natural

from hand import hand

class dealer:
    def __init__(self):
        pass


    def opening(self, deck):
        card_one = deck.deal()
        card_two = deck.deal()

        print(f"The dealer is dealt: {card_one}, Unknown")

        self.hand = hand(card_one, card_two)

        return deck


    def playRound(self, deck):
        print(f"The dealer has: {self.hand}")

        while self.hand.getValue() <= 16:
            new_card = deck.deal()
            print(f"The dealer is dealt: {new_card}")

            self.hand.addCard(new_card)
            print(f"The dealer has: {self.hand}")

        print("The dealer stays")
        return deck


    def checkNatural(self):
        print(f"The dealer has: {self.hand}")
        return(self.hand.getValue() == 21)


    def getValue(self):
        return self.hand.getValue()
