from utils.game import Board

new_game = Board()
new_game.start_game()

# COACHES' NOTES: The game works well! Nicely done!

# COACHES' NOTES: Your code is close to perfect. 
# Take these comments as tiny improvements, you have done an excellent job.
# - Good type hinting
# - Very nice docstring of functions
# - Very nice separation of code into methods and functions.
# - Very nice method names

# COACHES' NOTES: You misunderstood the inheritance in OOP. 
# It is not mandatory. Each class does not NEED to inherit from another. 
# You can have standlone classes. Inheritance is to share functionality and reduce code duplication.
# Thus, a Player inheriting from Card does not make sense.

# COACHES' NOTES: Another misunderstanding was the Card and Symbol class, how they are supposed to be used
# and how they interact with each other. They should have been used a objects, not as placeholders

# COACHES' NOTES: __str__() is supposed to help you have an easy way to print out the value of an object.
# It's perfect for this game, as it allows you to centralize how a card shall be printed on screen.
# class Card:
#   def __init__(self, value, icon):
#       self.value = value
#       self.icon = icon
#
# def __str__(self):
#   return f"{self.value} {self.icon}"
#
# if __name__=='__main__':
#   my_card = Card(value="A", icon="♣")
#   print(my_card) ---> prints out "A♣"
#       