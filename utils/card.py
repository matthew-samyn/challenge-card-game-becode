class Symbol():
    """ Class that stores the color and icon of a card. """
    def __init__(self):
        self.color = "RED"
        self.icon = "♥"

    def __str__(self):
        return f"Contains colour {self.color} and the card symbol:{self.icon}"

    def red_or_black(self, card: str):
        """
        Method to determine the colour of a card.
        :param card: A str containing the number and symbol of a card.
        :return: Alters self.color, either to BLACK OR RED
        """
        card_symbol = card[-1]
        red = ["♥", "♦"]
        black = ["♣", "♠"]
        if card_symbol in red:
            self.color = "RED"
        elif card_symbol in black:
            self.color = "BLACK"

class Card(Symbol):
    """ Class that stores the value of a card. """
    def __init__(self):
        super().__init__()
        self.value = "A"

    def __str__(self):
        return f"Inherits from class(Symbol) and contains the card value {self.value}"

