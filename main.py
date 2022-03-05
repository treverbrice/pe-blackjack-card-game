'''
TODO
X create a wait between each card reveal
X ask for number of shoes
X stop shuffling
X track num of cards seen
X track the count
record a guess and reveal the count
'''

from dealer import dealer
from player import player
from deck import deck
from count import count
import time

MINBET = 1

def getBet():
    tempBet = input("Place your bet: $")

    try:
        float(tempBet)
    except ValueError:
        print("Please enter a number")
        tempBet = getBet()

    if float(tempBet) < MINBET:
        print(f"The minimum bet is ${MINBET}")
        tempBet = getBet()

    return float(tempBet)


def askPlayAgain():
    if player.balance < MINBET:
        print("Your balance is too low to play.")
        return "no"

    print(f"\n{player.name}, you have ${player.balance}.", end = " ")
    playAgain = input(f"Would you like to play another hand? (yes) ")
    return playAgain


def resetHands(count, dealer, player):
    count.addCard(*dealer.hand.cards)
    count.addCard(*player.hand.cards)


def roundReset():
    resetHands(count, dealer, player)
    print(f"The current count is: {count.count}")
    print(f"cards dealt: {count.numCards()} out of: {shoes * 52}")
    playAgain = askPlayAgain()


# pre-game housekeeping
print("Welcome to Blackjack!\n")
print("This game is modified to help you practice counting cards")
print("2-6 = +1, 7-9 = 0, 10-A = -1\n")
name = input("What is your name? ")
shoes = int(input("How many shoes would you like? (1-6) "))
player = player(name, 500.0)
dealer = dealer()
deck = deck(shoes)
deck.shuffle()
count = count()


# main gameplay loop
print(f"\nWelcome, {player.name}, you have ${player.balance}.", end = " ")
playAgain = input(f"Would you like to play a hand? (yes) ")
while playAgain.lower() == "yes":
    bet = getBet()

    dealer.opening(deck)
    player.playRound(deck)

    # check for player getting a Natural
    if player.natural:
        if dealer.checkNatural():
            print("You both have 21. Your bet will be returned.")
            roundReset()
            continue
        else:
            print(f"Congrats {player.name}, you got a BlackJack!", end = " ")
            winnings = 1.5 * bet
            print(f"You won ${winnings}")
            player.adjustBalance(winnings)
            roundReset()
            continue
    # check for player busting
    elif player.getValue() > 21:
        print(f"Your hand value is over 21, you lose ${bet}")
        player.adjustBalance(-(bet))
        dealer.playRound(deck)
        roundReset()
        continue

    # player has a valid hand, dealers turn
    dealer.playRound(deck)

    # check for dealer busting
    if dealer.getValue() > 21:
        print(f"The dealer busted, you win ${bet}!")
        player.adjustBalance(bet)
        roundReset()
    # check for dealer winning
    elif dealer.getValue() > player.getValue():
        print(f"The dealer wins, you lose ${bet}")
        player.adjustBalance(-(bet))
        roundReset()
    # check for player winning
    elif dealer.getValue() < player.getValue():
        print(f"You won {player.name}! You win ${bet}")
        player.adjustBalance(bet)
        roundReset()
    # must be a tie
    else:
        print(f"You tied! Your bet will be returned to you")
        roundReset()

print(f"\n{player.name}, you left the game with ${player.balance}.")
print("Play again soon!")
