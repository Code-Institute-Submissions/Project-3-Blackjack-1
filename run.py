import random

class Card:
    def __init__(self, rank, suit):
        # Initializes the card with its rank and suit
        # and assigns it a value based on its rank
        self.rank = rank
        self.suit = suit
        if rank in ['10', 'Jack', 'Queen', 'King']:
            self.value = 10
        elif rank == 'Ace':
            self.value = 11
        else:
            self.value = int(rank)

           
class Deck:
    # Initializes the deck with 52 cards, each having a rank and suit
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = []
        # Initialize the deck of cards by iterating over each possible
        # combination of rank and suit and creating a new Card object for
        # each combination, which is then added to the self.cards list.
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

class Player:        


class Dealer:


class Game:


# main loop