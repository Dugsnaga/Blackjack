from files.walet import Walet

class Player():
    @classmethod
    def give_player(cls, name):
        new_player=Player(name)
        new_player.get_walet(Walet.add_walet_to_player(new_player))
        return new_player

    def __init__(self, name):
        self.name = name
        self.walet = None
        self.cards = []
        self.value = 0

    def __eq__(self, other):
       return self.value == other.value
    
    def __hash__(self):
        return hash(self.name)
    
    def __lt__(self,other):
        return self.value < other.value

    def __str__(self):
        return self.name
    

    def get_walet(self, walett):
        self.walet = walett

    def get_cards(self, lista):
        for card in lista:
            self.cards.append(card)
    
    def count_value(self):
        self.value = 0

        for card in self.cards:
            card_value = card.VALUE[card.rank]
            self.value += card_value
        
        if len(self.cards) == 2 and self.value == 22:
            self.value = 21

        if self.value > 21:
            self.value = 0
        
