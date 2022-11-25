
class Walet():
    CHIPS_VALUES = {
    1000 : "Black",
    500  : "Red",
    200  : "Gold",
    100  : "Green",
    50   : "Blue"
    }
    @classmethod
    def count_number_to_chips(cls, number, empty_dict):
        a=1
        while a==1:
            empty_dict.clear()
            a = a - 1

        for key, value in cls.CHIPS_VALUES.items():
            while number > key:
                empty_dict.setdefault(value, 0)
                empty_dict[value] += 1
                number= number - key

        if number == 50:
            if "Blue" not in empty_dict:
                empty_dict["Blue"] = 1
            if "Blue" in empty_dict:
                empty_dict["Blue"] += 1
        
    
    @classmethod
    def add_walet_to_player(cls, gracz):
        while True:
            starting_amount = input(f"Type amount of points {gracz} starts with(1-10000) ")
            zasieg = map(str, range(1, 10000))
            if starting_amount in zasieg:
                starting_amount_int = int(starting_amount)
                break
            if starting_amount not in zasieg:
                print("Your value is wrong, please type number between 1 and 10 000")
        begin_walet = Walet(starting_amount_int)
        return begin_walet
        

    def __init__(self, points):
        self.own_points = points
        self.own_chips = {}
        Walet.count_number_to_chips(number = self.own_points, empty_dict=self.own_chips)
        self.bet_points = 0
        self.bet_chips = {}
    
    def __eq__(self, other):
        return self.own_points == other.own_points 

    def raise_bet(self, amount):
        if amount > self.own_points:
            raise ValueError(f" You can't bet more than You have. Maksimum amount is {self.own_points}")
        self.bet_points += amount
        self.own_points = self.own_points - amount
        Walet.count_number_to_chips(number = self.own_points, empty_dict=self.own_chips)
        Walet.count_number_to_chips(number = self.bet_points, empty_dict=self.bet_chips)
    
    def lose_bet(self):
        self.bet_points = 0
        Walet.count_number_to_chips(number = self.bet_points, empty_dict=self.bet_chips)

    def win_bet(self):
        self.own_points = self.own_points + (self.bet_points*2)
        self.bet_points = 0
        Walet.count_number_to_chips(number = self.own_points, empty_dict=self.own_chips)
        Walet.count_number_to_chips(number = self.bet_points, empty_dict=self.bet_chips)

