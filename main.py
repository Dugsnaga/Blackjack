from files.card import Card
from files.deck import Deck
from files.game_round import GameRound
from files.player import Player
from files.walet import Walet
from files.bank import Bank

print("Starting game")

print("Created by DugSnaga")

while True:
    number_of_players = input("How many players would You like to have?(1-5) ")
    zasieg = ["1", "2", "3", "4", "5"]

    if number_of_players == "":
        print("Please type an integer ")
        continue
    
    if number_of_players not in zasieg:
        print("Number of players has to be between 1 and 5")
        continue
    
    if number_of_players in zasieg:
        break

petla = 0
players_names = []
while petla < int(number_of_players):
    while True:
        name = input("Write players name ")

        if name == "":
            print("name can't be empty")
            continue
        
        if name in players_names:
            print("Players names can't be the same. Please use another name!")
            continue

        if name not in players_names and name != "":
            print(f"Your name is {name}")
            players_names.append(name)
            petla += 1
            break


new_round = GameRound()
for gracz in players_names:
    new_round.add_players(Player.give_player(gracz))
new_round.add_bank(Bank.give_bank())

# new_round = GameRound()
# player1 = Player("player1")
# player2 = Player("player2")
# walet1 = Walet(1000)
# walet2 = Walet(1000)
# player1.walet = walet1
# player2.walet = walet2
# new_round.players = [player1, player2]


while True:
    eager_to_play = input("Do You wish to play new round?(y/n) ")
    
    if eager_to_play == "y":

        new_round.add_deck(Deck.give_ready_deck())
        new_round.play()
        continue
    if eager_to_play == "n":
        print("GAME OVER")
        print("Created by DugSnaga")

        break

    if eager_to_play != "y" and eager_to_play != "n":
        print("Please type 'y' or 'n'. Try one more time!")
        continue
    





