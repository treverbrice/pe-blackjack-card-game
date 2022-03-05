# player has name, and cash balance
# has a playRound method, that gets passed a deck, and makes a hand
# has adjustBalance method to give out winnings / take loses

from hand import hand
import time

class player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


    def _playerAction(self):
        response = input("Would you like to hit or stay? ")
        if response.lower() != 'hit' and response.lower() != 'stay':
            print("That is not a valid option")
            response = _playerAction()

        return response.lower()


    def playRound(self, deck):
        self.natural = False
        card_one = deck.deal()
        card_two = deck.deal()

        print(f"{self.name} is dealt: {card_one}")
        time.sleep(1)
        print(f"{self.name} is dealt: {card_two}")
        time.sleep(1)

        self.hand = hand(card_one, card_two)

        # check for natural
        if self.hand.getValue() == 21:
            self.natural = True
            return

        action = self._playerAction()
        while action == 'hit':
            new_card = deck.deal()
            print(f"{self.name} is dealt: {new_card}")
            time.sleep(1)
            self.hand.addCard(new_card)
            print(f"{self.name} now has: {self.hand}")
            time.sleep(1)

            # check for bust / 21
            if self.hand.getValue() >= 21:
                break
            action = self._playerAction()


    def adjustBalance(self, adjustment):
        self.balance += adjustment


    def getValue(self):
        return self.hand.getValue()
