class Bank():
    
    @classmethod
    def give_bank(cls):
        to_give = Bank()
        return to_give

    def __init__(self):
        self.hend = []
        self.value = 0
        self.eager = True
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self,other):
        return self.value < other.value
    
    def __len__(self):
        return len(self.hend)
    
    def get_cards(self, lista):
        for card in lista:
            self.hend.append(card)
    
    def count_value(self):
        self.value = 0

        for card in self.hend:
            card_value = card.VALUE[card.rank]
            self.value += card_value
        
        if len(self.hend) == 2 and self.value == 22:
            self.value = 21

        if self.value > 21:
            self.value = 0

    def is_eager(self, lista_graczy):
        self.count_value()
        wygrani = 0
        przegrani = 0
        lista_grajacych = []
        
        for gracz in lista_graczy:
            if gracz.value != 0:
                lista_grajacych.append(gracz)

        for gracz in lista_grajacych:
            if gracz > self:
                wygrani += 1
            else:
                przegrani +=1

        if wygrani == 0:
            self.eager = False
            
        else:
            if przegrani/wygrani > 1 and self.value > 16:
                self.eager = False
            if przegrani/wygrani == 1 and self.value > 17:
                self.eager = False
            if przegrani/wygrani < 1 and self.value > 18:
                self.eager = False
        if self.value == 0:
            self.eager = False
        
