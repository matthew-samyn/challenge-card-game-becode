from utils.player import Player
from utils.player import Deck
from itertools import chain
from itertools import repeat

class Board(Deck):
    def __init__(self):
        super().__init__()
        self.players = "" # list of PLAYERS
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []
        self.list_of_players = ["Maarten", "Anne", "Hoang Minh", "Matthew", "Leonor", "Jayesh"]
        self.list_of_class_Player = []
        self.dict_of_class_Player = {}

    def start_game(self):
        """ Assigns each name to a class instance of Player"""
        list_of_class_Player = []
        for player in self.list_of_players:
            self.list_of_class_Player.append(Player())
        self.dict_of_class_Player = {key: value for key, value in zip(self.list_of_players, self.list_of_class_Player)}
        self.get_game_ready()


    def get_game_ready(self):
        self.fill_deck()
        self.shuffle()
        self.play_the_cards(self.distribute(self.list_of_class_Player))

    def play_the_cards(self, card_per_player):
        for name in chain.from_iterable((repeat(self.list_of_players,card_per_player))):
            card_played = self.dict_of_class_Player[name].play(name)
            self.active_cards.append(card_played)
            if len(self.active_cards) > len(self.list_of_players):
                history_card = self.active_cards.pop(0)
                self.history_cards.append(history_card)
            self.turn_count += 1
            print(f"""
    Turn count: {self.turn_count}
    Last played cards: {self.active_cards}
    Number of cards out: {len(self.history_cards)}
    """)








