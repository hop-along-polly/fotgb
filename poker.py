class Card : 
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __eq__(self, obj):
        if self.suit == obj.suit and self.value == obj.value:
            return True
        return False
    def __str__(self):
        return f'{self.suit}:{self.value}'

class Hand :
    def __init__(self, cards, hand_limit):
        self.cards = cards
        self.hand_limit = hand_limit
    def __str__(self):
        result = ''
        for card in self.cards:
            result += str(card) + ', '
        return result

Hand1 = Hand([
    Card('spades', 8),
    Card('hearts', 8),
    Card('diamonds', 11),
    Card('hearts', 13),
    Card('clubs', 2)
], 5)



print(Hand1)