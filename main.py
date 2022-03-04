from dealer import dealer
from player import player
from deck import deck

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



# pre-game housekeeping
print("Welcome to Blackjack!\n")
name = input("What is your name? ")
player = player(name, 500.0)
dealer = dealer()
deck = deck()

# main gameplay loop
print(f"\nWelcome, {player.name}, you have ${player.balance}.", end = " ")
playAgain = input(f"Would you like to play a hand? (yes) ")
while playAgain.lower() == "yes":
    bet = getBet()
    deck.reset()
    deck.shuffle()

    dealer.opening(deck)
    player.playRound(deck)

    # check for player getting a Natural
    if player.natural:
        if dealer.checkNatural():
            print("You both have 21. Your bet will be returned.")
            playAgain = askPlayAgain()
            continue
        else:
            print(f"Congrats {player.name}, you got a BlackJack!", end = " ")
            winnings = 1.5 * bet
            print(f"You won ${winnings}")
            player.adjustBalance(winnings)
            playAgain = askPlayAgain()
            continue
    # check for player busting
    elif player.getValue() > 21:
        print(f"Your hand value is over 21, you lose ${bet}")
        player.adjustBalance(-(bet))
        playAgain = askPlayAgain()
        continue

    # player has a valid hand, dealers turn
    dealer.playRound(deck)

    # check for dealer busting
    if dealer.getValue() > 21:
        print(f"The dealer busted, you win ${bet}!")
        player.adjustBalance(bet)
        playAgain = askPlayAgain()
    # check for dealer winning
    elif dealer.getValue() > player.getValue():
        print(f"The dealer wins, you lose ${bet}")
        player.adjustBalance(-(bet))
        playAgain = askPlayAgain()
    # check for you winning
    elif dealer.getValue() < player.getValue():
        print(f"You won {player.name}! You win ${bet}")
        player.adjustBalance(bet)
        playAgain = askPlayAgain()
    # must be a tie
    else:
        print(f"You tied! Your bet will be returned to you")
        playAgain = askPlayAgain()

print(f"\n{player.name}, you left the game with ${player.balance}.")
print("Play again soon!")
