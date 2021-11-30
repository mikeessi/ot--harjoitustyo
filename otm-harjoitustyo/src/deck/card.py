class Card:

    suits = ["diamonds", "clubs", "hearts", "spades"]

    values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
        if suit in [0,2]:
            self.color = "Red"
        else:
            self.color = "Black"

    def __repr__(self):
        name = str(self.suit) + "_" + str(self.value)+".png"
        return name
