'''import card

test = card.card('spade', 'a')
value = test.getValue()
card = test.toStr()

print(value)
print(card)'''

'''import deck

my_cards = deck.deck()
print(my_cards.cards)
my_cards.shuffle()
print(my_cards.cards)

half_deck = []
for i in range(26):
    one_card = my_cards.deal()
    half_deck.append(one_card)

print(half_deck)
print(my_cards.cards)'''

'''import hand
import deck
import card

my_deck = deck.deck()
my_deck.shuffle()

my_hand = hand.hand(my_deck.deal(), my_deck.deal())
print(my_hand.cards)
print(my_hand.getValue())

card1 = card.card('spade', 'a')
card2 = card.card('heart', 'k')
card3 = card.card('diamond', 'a')
card4 = card.card('club', '4')
new_hand = hand.hand(card1, card3, card4)
print(new_hand.cards)
print(new_hand.getValue())'''

import player
import deck

name = "Trever"
balance = 500

my_player = player.player(name, balance)
my_deck = deck.deck()
my_deck.shuffle()

my_player.playRound(my_deck)
