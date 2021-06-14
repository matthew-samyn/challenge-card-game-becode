class Symbol():
    """ Class that stores the color and icon of a card. """
    def __init__(self):
        # COACHES' NOTES: You should have gotten the icon as parameter.
        # Moreover, self.color would have been inferred from the icon, just
        # like you did in `self.red_or_black()`
        # def __init__(self, icon):
        #   self.color = self.red_or_black()
        #   self.icon = icon
        self.color = "RED" 
        self.icon = "♥"

    def __str__(self):
        return f"Contains colour {self.color} and the card symbol:{self.icon}"

        # COACHES' NOTES: Red or black has to the symbol (self.icon) as we are in the Symbol class.
        # No need to pass it as argument to the function.
    def red_or_black(self, card: str):
        """
        Method to determine the colour of a card.
        :param card: A str containing the number and symbol of a card.
        :return: Alters self.color, either to BLACK OR RED
        """
        card_symbol = card[-1]  #COACHES' NOTES: card_symbol should be replaced by self.icon
        red = ["♥", "♦"]
        black = ["♣", "♠"]

        # COACHES' NOTES: It's better to return the color rather than modify it in place.
        # Doing it like you do here, you never know when the value of the self.color variable
        # actually changes, making it unpredictable.
        if card_symbol in red:
            self.color = "RED"
        elif card_symbol in black:
            self.color = "BLACK"

class Card(Symbol):
    """ Class that stores the value of a card. """
    # COACHES' NOTES: The Card object right now does nothing.
    # It should have the value and the icon as parameter, 
    # the latter being passed to the Symbol class.
    def __init__(self):
        super().__init__()
        self.value = "A"

    def __str__(self):
        return f"Inherits from class(Symbol) and contains the card value {self.value}"

