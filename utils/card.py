class Symbol():
    def __init__(self):
        self.color = "RED"
        self.icon = "♥"

    def __str__(self):
        return f"Contains colour {self.color} and the card symbol:{self.icon}"


class Card(Symbol):
    def __init__(self):
        super().__init__()
        self.value = "A"

    def __str__(self):
        return f"Inherits from class(Symbol) and contains the card value {self.value}"