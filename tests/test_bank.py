import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from files.game_round import GameRound
from files.card import Card
from files.deck import Deck
from files.player import Player
from files.walet import Walet
from files.bank import Bank

class BankTest(unittest.TestCase):
    def test_has_cards_atr_empty_list(self):
        bank = Bank()
        self.assertEqual(bank.hend, [])
    
    def test_has_attr_eager_as_True_at_start(self):
        bank = Bank()
        self.assertEqual(bank.eager, True)

    def test_is_eager_player_0(self):
        player1 = Player("player1")
        player2 = Player("player2")
        bank = Bank()
        bank.is_eager([player1, player2])
        self.assertEqual(bank.eager, False)
    
    def test_is_eager_player_17(self):
        player1 = Player("player1")
        player2 = Player("player2")
        player1.value = 17
        player2.value = 5
        bank = Bank()
        card = Card ("Hearts", "2")
        bank.hend = [card]
        bank.is_eager([player1, player2])
        self.assertEqual(bank.eager, True)


    def test_get_cards(self):
        bank = Bank()
        cards = [MagicMock, MagicMock]
        bank.get_cards(cards)
        self.assertEqual(bank.hend, cards)
    
    def test_bank_has_value_atr_equal_to_0(self):
        bank = Bank()
        self.assertEqual(bank.value, 0)

    def test_count_bank_value_according_to_cards(self):
        card1 = Card("Hearts", "Ace")
        card2 = Card("Diamonds", "10")
        player1 = Bank()
        player1.hend = [card1, card2]
        player1.count_value()
        self.assertEqual(player1.value, 21)
    
    def test_bank_knows_how_to_equal_and_unequal(self):
        bank1 = Bank()
        bank2 = Bank()
        Bank3 = Bank()
        bank1.value = 5
        self.assertEqual(bank1>bank2, True)
        self.assertEqual(bank2==Bank3, True)        

    def test_bank_knows_how_to_compare_with_player(self):
        card1 = Card("Hearts", "Ace")
        card2 = Card("Diamonds", "10")
        player1 = Player("player1")
        player2 = Player("player2")
        bank1 = Bank()
        player1.cards = [card1, card2]
        player2.cards = [card1]
        bank1.hend = [card1, card2]
        player2.count_value()
        player1.count_value()
        bank1.count_value()
        self.assertEqual(bank1==player1, True)
        self.assertEqual(bank1>player2, True)
        
    def test_instiation_and_giving_function(self):
        a = Bank.give_bank()
        self.assertIsInstance(a, Bank)
        self.assertEqual(a.value, 0)


        