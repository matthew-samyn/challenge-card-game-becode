from utils.player import Player
from utils.player import Deck
from itertools import chain
from itertools import repeat

class Board(Deck): # COACHES' NOTES: Board should not interhit from Deck.
    """
    Class that handles a cardgame between a number of players.

    Inherits from Deck
    """
    def __init__(self):
        super().__init__()
        self.players = ["Maarten", "Anne", "Hoang Minh", "Matthew", "Leonor", "Jayesh"]
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []
        self.list_of_class_Player = []
        self.dict_of_class_Player = {}

    def __str__(self):
        return f"Inherits from class(Deck). Using method start_game() will kick off a sequence of events."

    def creating_classes_for_each_player(self):
        """
        Method that assigns each name to a class instance of Player
        Saves it in a list and dict {name: class instance}
        """
        #COACHES' NOTES: It would have been easier to add a name property to the Player class.
        # THis would have also made it so that you can just a variable like `list_of_players`,
        # instead of sometimes using `list_of_class_Player`, `players` and other times `dict_of_class_Player`.
        for player in self.players:
            self.list_of_class_Player.append(Player())
            self.dict_of_class_Player = {key: value for key, value in zip(self.players, self.list_of_class_Player)}

    def start_game(self):
        """
        Methods that starts the cardgame.
        Calls methods inherited from Deck.

        :return: Calls method self.play_the_cards()
        """
        self.creating_classes_for_each_player()
        self.fill_deck()
        self.shuffle()
        cards_each = self.distribute(self.list_of_class_Player)
        self.play_the_cards(cards_each)

    def play_the_cards(self, card_per_player: int):
        """
        Method that makes every player play all of his cards until there are no more left.

        :param card_per_player: An int containing the number of cards each player has.
        :return: Calls method to print an informative message on the status of the game.
        """
        # COACHES' NOTES: It is really hard to understand what the next line does
        player_lst_equal_to_number_of_cards = chain.from_iterable(repeat(self.players, card_per_player))
        for name in player_lst_equal_to_number_of_cards:
            card_played = self.dict_of_class_Player[name].play(name) # Calls method .play() of a Player instance.
            self.display_after_each_turn(card_played)

    def display_after_each_turn(self, card_played: str):
        """
        Method to print an informative message on the status of the game.

        :param card_played: A str containing the last card played.
        :return: Prints an informative message on screen.
        """
        self.active_cards.append(card_played)
        if len(self.active_cards) > len(self.players):
            history_card = self.active_cards.pop(0)
            self.history_cards.append(history_card)
        self.turn_count += 1
        print(f"""
    Turn count: {self.turn_count}
    Last played cards: {self.active_cards}
    Number of cards out: {len(self.history_cards)}
    """)








