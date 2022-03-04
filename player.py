# player has name, and cash balance
# has a playRound method, that gets passed a deck, and makes a hand
# has adjustBalance method to give out winnings / take loses

from hand import hand

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
        '''
        This method returns True if the player draws a natural 21
        '''
        self.hand = hand(deck.deal(), deck.deal())
        print(f"{self.name} is dealt: {self.hand}")

        # check for natural
        if self.hand.getValue() == 21:
            return True

        action = self._playerAction()
        while action == 'hit':
            new_card = deck.deal()
            print(f"{self.name} is dealt: {new_card}")
            self.hand.addCard(new_card)
            print(f"{self.name} now has: {self.hand}")

            # check for bust / 21
            if self.hand.getValue() >= 21:
                break
            action = self._playerAction()

        return False


    def adjustBalance(self, adjustment):
        self.balance += adjustment


    def getValue(self):
        return self.hand.getValue()
