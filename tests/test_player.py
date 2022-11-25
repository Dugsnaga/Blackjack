import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from files.player import Player
from files.game_round import GameRound
from files.card import Card
from files.deck import Deck
from files.walet import Walet


class PlayerTest(unittest.TestCase):
    def test_player_has_value_atr_equal_to_0(self):
        player = Player("player1")
        self.assertEqual(player.value, 0)

    def test_class_player_has_name_atr(self):
        player = Player("player1")
        self.assertEqual(player.name, "player1")
    
    def test_get_walet(self):
        walet = MagicMock
        player1 = Player("player1")
        player1.get_walet(walet)
        self.assertEqual(player1.walet, walet)

    def test_start_with_empty_hand(self):
        player1 = Player("player1")
        self.assertEqual(player1.cards, [])

    def test_get_cards(self):
        card1 = MagicMock
        card2 = MagicMock
        cards = [card1, card2]
        player1 = Player("player1")
        player1.get_cards(cards)
        self.assertEqual(player1.cards, [card1, card2] )
    
    @patch('files.walet.input')
    def test_give_player_to_round(self, mock_input):
        mock_input.return_value = "1000"
        a = Player.give_player("player1")
        self.assertIsInstance(a, Player)

    def test_player_is_printible_in_human_friendly_way(self):
        player1 = Player("player1")
        self.assertEqual(player1.__str__() , "player1")
    
    def test_count_players_value_according_to_cards(self):
        card1 = Card("Hearts", "Ace")
        card2 = Card("Diamonds", "10")
        player1 = Player("player1")
        player1.cards = [card1, card2]
        player1.count_value()
        self.assertEqual(player1.value, 21)
    
    
    
    def test_player_knows_how_to_equal_and_unequal(self):
        card1 = Card("Hearts", "Ace")
        card2 = Card("Diamonds", "10")
        player1 = Player("player1")
        player2 = Player("player2")
        player3 = Player("player3")
        player1.cards = [card1, card2]
        player2.cards = [card1]
        player3.cards = [card1]
        player1.count_value()
        self.assertEqual(player1>player2, True)
        self.assertEqual(player3==player2, True)





        



# python.exe -m unittest discover tests