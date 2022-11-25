import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from files.game_round import GameRound
from files.card import Card
from files.deck import Deck
from files.player import Player
from files.walet import Walet
from files.bank import Bank

class GameRoundTest(unittest.TestCase):

    def test_game_round_has_no_players_at_start(self):
        rund = GameRound()
        self.assertEqual( rund.players, [] )

    def test_add_deck(self):
        rund = GameRound()
        rund.add_deck(Deck.give_ready_deck())
        self.assertIsInstance(rund.deck, Deck)
        self.assertEqual(len(rund.deck), 52)


    def test_add_players(self):
        player1 = MagicMock
        player2 = MagicMock
        gracze = [player1, player2]
        rund = GameRound()
        rund.add_players(player1)
        rund.add_players(player2)
        self.assertEqual(rund.players, gracze)
    
    def test_add_bank(self):
        bank = MagicMock
        rund = GameRound()
        rund.add_bank(bank)
        self.assertEqual(rund.bank, bank)
    
    def test_GameRound_has_atributes_bet_players_and_draw_players_as_empty_dict(self):
        rund = GameRound()
        self.assertEqual(rund.bet_players, {})
        self.assertEqual(rund.draw_players, {})

    def test_GameRund_has_bank_attribute_None_at_beginning(self):
        rund = GameRound()
        self.assertEqual(rund.bank, None)

    @patch('files.game_round.input')
    def test_ask_for_first_bets(self, mock_input):
        mock_input.return_value = "100"
        rund = GameRound()
        rund.add_deck(Deck.give_ready_deck())
        player1 = Player("player1")
        player2 = Player("player2")
        walet1 = Walet(1000)
        walet2 = Walet(1000)
        player1.get_walet(walet1)
        player2.get_walet(walet2)
        rund.add_players(player1, player2)
        rund.ask_for_first_bets()
        self.assertEqual(rund.bet_players, {player1 : 100, player2 : 100})


    def test_bets(self):
        rund = GameRound()
        rund.add_deck(Deck.give_ready_deck())
        player1 = Player("player1")
        player2 = Player("player2")
        walet1 = Walet(1000)
        walet2 = Walet(1000)
        player1.get_walet(walet1)
        player2.get_walet(walet2)
        rund.add_players(player1, player2)
        rund.bet_players = {player1 : 100, player2 : 50}
        rund.bets()
        self.assertEqual(player1.walet.own_points, 900)
        self.assertEqual(player2.walet.own_points, 950)
        self.assertEqual(player1.walet.bet_points, 100)
        self.assertEqual(player2.walet.bet_points, 50)

    def test_deal_2_first_cards_to_players_and_a_bank(self):
        rund = GameRound()
        bank = Bank()
        rund.add_deck(Deck.give_ready_deck())
        rund.add_bank(bank)
        player1 = Player("player1")
        player2 = Player("player2")
        player3 = Player("player3")
        rund.add_players(player1, player2, player3)
        rund.deal_2_first_cards_to_players_and_a_bank()
        self.assertEqual( len(player1.cards), 2 )
        self.assertEqual( len(player2.cards), 2 )
        self.assertEqual( len(player3.cards), 2 )
        self.assertEqual( len(rund.bank), 2 )
        self.assertIsInstance(player1.cards[0], Card )
        self.assertIsInstance(rund.bank.hend[0], Card )

    @patch('files.game_round.input')
    def test_ask_for_next_bet_with_no(self, mock_input):
        mock_input.return_value = "0"
        rund = GameRound()
        rund.add_deck(Deck.give_ready_deck())
        player1 = Player("player1")
        player2 = Player("player2")
        player3 = Player("player3")
        walet1 = Walet(1000)
        walet2 = Walet(1000)
        walet3 = Walet(1000)
        player1.get_walet(walet1)
        player2.get_walet(walet2)
        player3.get_walet(walet3)
        rund.add_players(player1, player2, player3)
        rund.draw_players = {player1 : True, player2: True, player3 : True }
        rund.bet_players = {player1 : 100, player2 : 200}
        rund.ask_for_next_bet()
        self.assertEqual(len(rund.bet_players), 0)
    

    @patch('files.game_round.input')
    def test_ask_for_next_bet_with_100(self, mock_input):
        mock_input.return_value = "100"
        rund = GameRound()
        rund.add_deck(Deck.give_ready_deck())
        player1 = Player("player1")
        player2 = Player("player2")
        player3 = Player("player3")
        walet1 = Walet(1000)
        walet2 = Walet(1000)
        walet3 = Walet(1000)
        player1.get_walet(walet1)
        player2.get_walet(walet2)
        player3.get_walet(walet3)
        rund.add_players(player1, player2, player3)
        rund.draw_players = {player1 : True, player2: True, player3 : True }
        rund.bet_players = {player1 : 100, player2 : 200}
        rund.ask_for_next_bet()
        self.assertEqual(len(rund.bet_players), 3)
        self.assertEqual(rund.bet_players[player1], 100)
        self.assertEqual(rund.bet_players[player2], 100)
        self.assertEqual(rund.bet_players[player3], 100)


    @patch('files.game_round.input')
    def test_ask_if_need_additional_card(self, mock_input):
        mock_input.return_value = "n"
        rund = GameRound()
        rund.add_deck(Deck.give_ready_deck())
        player1 = Player("player1")
        player2 = Player("player2")
        player3 = Player("player3")
        rund.add_players(player1, player2, player3)
        rund.draw_players = {player2: True, player3 : True }
        rund.bet_players = {player2 : 200}
        rund.ask_if_need_additional_card()
        self.assertEqual(len(rund.bet_players), 1)
        self.assertNotIn(player1, rund.bet_players)
        self.assertIn(player2, rund.bet_players)
        self.assertNotIn(player3, rund.bet_players)

    def test_give_additional_card(self):
        rund = GameRound()
        rund.add_deck(Deck.give_ready_deck())
        player1 = Player("player1")
        player2 = Player("player2")
        player3 = Player("player3")
        rund.add_players(player1, player2, player3)
        rund.draw_players = {player2: True, player3 : True }
        rund.bet_players = {player2 : 200}
        rund.give_additional_card()
        self.assertEqual(len(player1.cards), 0)
        self.assertEqual(len(player2.cards), 1)
        self.assertEqual(len(player3.cards), 1)
        self.assertIsInstance(player2.cards[0], Card)
        self.assertIsInstance(player3.cards[0], Card)
    
    def test_count_all_players(self):
        rund = GameRound()
        player1 = Player("player1")
        player2 = Player("player2")
        player3 = Player("player3")
        card1 = Card(suit = "Hearts", rank =  "2")
        card2 = Card(suit = "Spades", rank = "Ace")
        player1.cards = [card1, card2]
        player2.cards = [card1]
        rund.add_players(player1, player2)
        rund.count_players()
        self.assertEqual(player1.value, 13)
        self.assertEqual(player2.value, 2)
        self.assertEqual(player3.value, 0)
    
    def test_count_bank(self):
        rund = GameRound()
        bank = Bank()
        deck = Deck.give_ready_deck()
        rund.deck = deck
        player1 = Player("player1")
        player2 = Player("player2")
        card1 = Card(suit = "Hearts", rank =  "2")
        card2 = Card(suit = "Spades", rank = "Ace")
        player1.cards = [card1, card2]
        player2.cards = [card1]
        rund.add_players(player1, player2)
        bank.hend = [card1]
        rund.add_bank(bank)
        rund.count_players()
        rund.count_bank()
        self.assertEqual(len(bank)>1, True)
        self.assertEqual(bank.eager, False)

    def test_check_win(self):
        rund = GameRound()
        bank = Bank()
        player1 = Player("player1")
        player2 = Player("player2")
        player1.value = 21
        player2.value = 13
        rund.add_players(player1, player2)
        bank.value = 18
        rund.add_bank(bank)
        rund.check_win()
        self.assertEqual(len(rund.bet_players), 2)
        self.assertEqual(rund.bet_players[player1], True)
        self.assertEqual(rund.bet_players[player2], False)
    
    def test_count_stakes(self):
        rund = GameRound()
        player1 = Player("player1")
        player2 = Player("player2")
        player3 = Player("player3")
        walet1 = Walet(1000)
        walet2 = Walet(1000)
        walet3 = Walet(1000)
        walet1.bet_points = 100
        walet2.bet_points = 0
        walet3.bet_points = 100
        player1.walet = walet1
        player2.walet = walet2
        player3.walet = walet3
        rund.bet_players = {player1 : True, player2 : True, player3 : False}
        rund.count_stakes()
        self.assertEqual(player1.walet.bet_points, 0)
        self.assertEqual(player2.walet.bet_points, 0)
        self.assertEqual(player3.walet.bet_points, 0)
        self.assertEqual(player1.walet.own_points, 1200)
        self.assertEqual(player2.walet.own_points, 1000)
        self.assertEqual(player3.walet.own_points, 1000)

    def test_remove_broke(self):
        rund = GameRound()
        player1 = Player("player1")
        walet1 = Walet(0)
        player1.walet = walet1
        rund.players = [player1]
        rund.remove_broke()
        self.assertNotIn(player1, rund.players)

    def test_remove_deck(self):
        rund = GameRound()
        deck = Deck()
        rund.deck = deck
        rund.remove_deck()
        self.assertEqual(rund.deck, None)



        




        
    



# python.exe -m unittest discover tests