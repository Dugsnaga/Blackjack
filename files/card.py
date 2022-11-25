

class Card():
    SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]
    RANKS = [
                "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "Jack", "Queen", "King", "Ace"
            ]
    VALUE = {
        "2"     : 2,
        "3"     : 3,
        "4"     : 4, 
        "5"     : 5,
        "6"     : 6,
        "7"     : 7,
        "8"     : 8,
        "9"     : 9,
        "10"    : 10,
        "Jack"  : 2,
        "Queen" : 3,
        "King"  : 4,
        "Ace"   : 11
    }
    ALL_CARDS = []

    @classmethod
    def create_all(cls):
        a=1
        while a==1:
            cls.ALL_CARDS = []
            a += 1
        for suit in cls.SUITS:
            for rank in cls.RANKS:
                new_card = Card(suit = suit, rank = rank)
                cls.ALL_CARDS.append(new_card)


    def __init__(self, suit, rank):
        if suit not in Card.SUITS:
            raise ValueError(f"{suit}, is not a valid suit. Please choose one of theese {Card.SUITS}")
        if rank not in Card.RANKS:
            raise ValueError(f"{rank}, is not a valid suit. Please choose one of theese {Card.RANKS}")
        self.suit = suit
        self.rank = rank
        cp_value = Card.VALUE[rank]
        self.value = cp_value
        
    def __add__(self, other):
        return self.value + other.value
    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    def __eq__(self, other):
        return self.rank==other.rank and self.suit==other.suit