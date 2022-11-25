from files.card import Card
from files.deck import Deck
from files.player import Player
from files.walet import Walet

class GameRound():
    def __init__(self):
        self.players = []
        self.deck = None
        self.bank = None
        self.bet_players = {}
        self.draw_players = {}
    
    def add_deck(self, deck):
        self.deck = deck
    
    def add_players(self, *args):
        for player in args:
            self.players.append(player)

    def add_bank(self, bank):
        self.bank = bank
    
    def play(self):
        self.ask_for_first_bets()
        self.bets()
        self.deal_2_first_cards_to_players_and_a_bank()
        self.ask_for_next_bet()
        
        while len(self.draw_players) > 0:
            self.bets()
            self.ask_if_need_additional_card()
            self.give_additional_card()
            self.ask_for_next_bet()
        
        self.count_players()
        self.count_bank()
        self.check_win()
        self.count_stakes()
        self.remove_broke()
        self.remove_deck()

    def ask_for_first_bets(self):
        for gracz in self.players:
            while True:
                input_bet_amount = input(f"{gracz}  How much would you like to bet? Min is 1 Max is {gracz.walet.own_points} ")
                a = range(1, (gracz.walet.own_points + 1)) 
                zasieg = list(map(str, a))
                if input_bet_amount in zasieg:
                    int_bet_amount = int(input_bet_amount)
                    self.bet_players[gracz] = int_bet_amount
                    break

                if input_bet_amount not in zasieg:
                    print(f"{gracz} Your bet amount is {input_bet_amount}. It need to be in range 1-{gracz.walet.own_points}")
                    continue
                            
    def bets(self):
        for gracz, stake in self.bet_players.items():
            gracz.walet.raise_bet(stake)

    def deal_2_first_cards_to_players_and_a_bank(self):
        number_of_players_plus_two = 2* (len(self.players)) + 2
        list_of_cards = self.deck.give_cards(number_of_players_plus_two)
        for gracz in self.players:
            dwie = list_of_cards[:2]
            gracz.get_cards(dwie)
            del list_of_cards[:2]
            self.draw_players[gracz] = True
       
        self.bank.get_cards(list_of_cards)
        print(f"House has two cards, one of which is {self.bank.cards[0]}")

    def ask_for_next_bet(self):
        self.bet_players = {}
        lista_to_remove = []
        for gracz in self.draw_players:
            self.count_players()
            while True:
                input_bet_amount = input(f"{gracz} Your cards are {gracz.cards} it is {gracz.value} points You already beted {gracz.walet.bet_points} \nHow much would you like to bet? Min is 1 Max is {gracz.walet.own_points}. If You don't want to bet type '0' ")
                a = range(1, (gracz.walet.own_points + 1)) 
                zasieg = list(map(str, a))
                if input_bet_amount in zasieg:
                    int_bet_amount = int(input_bet_amount)
                    self.bet_players[gracz] = int_bet_amount
                    break
                
                if input_bet_amount == "0":
                    break

                if input_bet_amount not in zasieg and input_bet_amount != "0":
                    print(f"{gracz} Your bet amount is {input_bet_amount}. It need to be in range 0-{gracz.walet.own_points}")
                    continue
          

    def ask_if_need_additional_card(self):
        list_to_remove = []
        for gracz in self.draw_players:
            if gracz in self.bet_players:
                continue
            else:
                while True:
                    draw_input = input(f"{gracz} Your cards are{gracz.cards} it is {gracz.value} points. Do You wish additional card (y/n) ")
                
                    if draw_input == "n":
                        gracz.count_value()
                        list_to_remove.append(gracz)
                        print(f"You have passed with {gracz.cards}. Your points are {gracz.value}. Good luck with that!")########!!!!!!!!!!!!!!!!!!!#########################
                        break
                    if draw_input == "y":
                        break
                    if draw_input != "y" and draw_input != "n":
                        print("Your input is invalid. Type 'y' or 'n' ")
            
        for el in list_to_remove:
            del self.draw_players[el]

    def give_additional_card(self): #and remove busted
        list_to_remove = []
        for gracz in self.draw_players:
            new_card = self.deck.give_cards(1)
            gracz.get_cards(new_card)
            gracz.count_value()
            if gracz.value == 0:
                print(f"{gracz} You have busted. With {gracz.cards}. You've lost this round!")
                list_to_remove.append(gracz)

        for el in list_to_remove:
            del self.draw_players[el]
        


    def count_players(self):
        for gracz in self.players:
            gracz.count_value()
    
    def count_bank(self):
        self.bank.is_eager(self.players)
        while self.bank.eager == True:
            print("Dealer shouts to himself: 'HIT ME!'")#############################!!!!!!!!!!!!!!!!!!!!!!!#######################
            new_card = self.deck.give_cards(1)
            self.bank.get_cards(new_card)
            self.bank.is_eager(self.players)
            print(f"House has {self.bank.hend}")
    
    def check_win(self):
        self.bet_players = {}
        for gracz in self.players:
            if gracz > self.bank:
                self.bet_players[gracz] = True
            else:
                self.bet_players[gracz] = False
    
    def count_stakes(self):
        for gracz, win in self.bet_players.items():
            if win == True:
                print(f"{gracz} won {gracz.walet.bet_points} with {gracz.cards}. You have now {gracz.walet.own_points} points")
                gracz.walet.win_bet()
            if win == False:
                print(f"{gracz} lost {gracz.walet.bet_points} with {gracz.cards}. You have now {gracz.walet.own_points} points")
                gracz.walet.lose_bet()

        self.bet_players == {}
        
   
    def remove_broke(self):
        for gracz in self.players:
            if gracz.walet.own_points == 0:
                self.players.remove(gracz)
                print(f"{gracz} is broke. Ha has been removed from play. Go home!")
    
    def remove_deck(self):
        self.deck = None
        

        
#end_game, count_bank, count_winners, count_stakes

    
                
            
