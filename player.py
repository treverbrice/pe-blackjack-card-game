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
        my_hand = hand(deck.deal(), deck.deal())
        print(f"{self.name} is dealt: {my_hand}")

        # check for natural
        if my_hand.getValue() == 21:
            return(21, True)

        action = self._playerAction()
        while action == 'hit':
            new_card = deck.deal()
            print(f"{self.name} is dealt: {new_card}")
            my_hand.addCard(new_card)
            print(f"{self.name} now has: {my_hand}")
            
            # check for bust / 21
            if my_hand.getValue() >= 21:
                break
            action = self._playerAction()

        return(my_hand.getValue(), False)


    def adjustBalance(self, adjustment):
        self.balance += adjustment
