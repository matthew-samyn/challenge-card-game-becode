from utils.card import Card
from random import choice
from random import shuffle
from time import sleep

class Player(Card):
    def __init__(self):
        super().__init__()
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = len(self.cards)
        self.history = []

    def __str__(self):
        return f"Inherits from class(Card). Makes people play their card."

    def play(self, name):
        sleep(choice([0.5, 1, 1.5]))
        self.turn_count += 1
        card_played = choice(self.cards)
        self.cards.remove(card_played)
        self.history.append(card_played)
        print(f"{name} {self.turn_count} played: {card_played[:-1]} {card_played[-1]}")
        return card_played




class Deck(Player):
    def __init__(self):
        super().__init__()
        self.cards = []

    def __str__(self):
        return f"Inherits from class(Player). Creates the deck of cards, shuffles and distributes it."

    def fill_deck(self):
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        symbols = ["♥", "♦", "♣", "♠"]
        for symbol in symbols:
            for value in values:
                self.cards.append(value+symbol)

    def shuffle(self):
        shuffle(self.cards)

    def distribute(self, classes): #list van player als argument
        number_of_players = len(classes)
        cards_left = 52 % number_of_players
        card_per_player = int((52 - cards_left) / number_of_players)
        for player in classes:
            for number in range(card_per_player):
                card = self.cards.pop()
                player.cards.append(card)
        return card_per_player








deck = Deck()
deck.fill_deck()
deck.shuffle()










