from utils.card import Card
from random import choice
from random import shuffle
from time import sleep
from typing import List

class Player(Card): # COACHES' NOTES: Player should not interhit from Card.
    """
    Class assigned to each player in a cardgame.

    Inherits from Card"""
    def __init__(self):
        super().__init__()
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = len(self.cards)
        self.history = []

    def __str__(self):
        return f"Inherits from class(Card). Makes people play their card."

    def play(self, name: str) -> str:
        """
        Function that makes Player play one of his cards.

        :param name: A str containing the name of the player.
        :return: A string of the cards being played.
        """
        # COACHES' NOTES: Best practices with the random library is to just do `import random`.
        # and do random.choice(...). It makes it easier to see that the choice method comes from random.
        sleep(choice([0.5, 1, 1.5]))
        self.turn_count += 1
        card_played = choice(self.cards)
        self.cards.remove(card_played)
        self.history.append(card_played)
        self.icon = card_played[-1]
        self.value = card_played[:-1]
        #COACHES' NOTES: It would have been easier to add a `name` property to the Player class.
        print(f"{name} {self.turn_count} played: {self.value} {self.icon}")
        return card_played




class Deck(Player): # COACHES' NOTES: Deck should not interhit from Player.
    """
    Class to create a deck of cards.

    Inherits from Player
    """
    def __init__(self):
        super().__init__()
        self.cards = []

    def __str__(self):
        return f"Inherits from class(Player). Creates the deck of cards, shuffles and distributes it."

    def fill_deck(self):
        """
        Method that generates a full deck of 52 cards.

        :param self.cards: Appends the 52 cards to this param.
        """
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        symbols = ["♥", "♦", "♣", "♠"]
        for symbol in symbols:
            for value in values:
                #COACHES' NOTES: This list of cards should hold Card objects, not strings.
                self.cards.append(value+symbol)

    def shuffle(self):
        """
        Method that shuffles the cards in self.cards
        """
        shuffle(self.cards)

    def distribute(self, classes: List) -> int:
        """
        Method that distributes a deck of cards evenly among number of players (class instances).
        :param classes: Contains a List of class -> Player instances.
        :return: An int containing number of cards per player.
        """
        number_of_players = len(classes)
        cards_left = 52 % number_of_players
        card_per_player = int((52 - cards_left) / number_of_players)
        for player in classes:
            for number in range(card_per_player):
                card = self.cards.pop()
                player.cards.append(card)
        return card_per_player










