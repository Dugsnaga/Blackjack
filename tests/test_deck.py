import unittest
from unittest.mock import patch
from unittest.mock import MagicMock


from files.deck import Deck
from files.card import Card

class DeckTest(unittest.TestCase):

    def test_store_no_cards_at_the_begining(self):
        deck = Deck()
        self.assertEqual(
            deck.cards, 
            []
        )
    def test_if_len_function_gives_number_of_the_cards(self):
        deck = Deck()
        self.assertEqual(
            len(deck),
            0
        )
    def test_for_filling_deck_with_cards(self):
        deck = Deck()
        card = Card(suit = "Spades", rank = "Ace")
        deck.fill_deck_with_all_cards()
        self.assertEqual(len(deck),52)
        self.assertIsInstance(deck.cards[1], Card)
        self.assertEqual(card, deck.cards[-1])
        
    @patch("random.shuffle")
    def test_if_shuffle_is_working(self, mock_shuffle):
        deck=Deck()
        deck.fill_deck_with_all_cards()
        copy_deck = deck.cards[:]
        deck.shuffle()
        mock_shuffle.assert_called_once_with(deck.cards)

        self.assertNotEqual(
            deck,
            copy_deck
        )

    def test_give_cards(self):
        deck=Deck()
        deck.fill_deck_with_all_cards()
        deck.shuffle()
        a = deck.cards[0]
        b = deck.cards[1]
        c = deck.cards[2]
        d = list(deck.give_cards(3))
        self.assertEqual(d[0], a)
        self.assertEqual(d[1], b)
        self.assertEqual(d[2], c)
        self.assertNotIn(a, deck.cards)
        self.assertNotIn(b, deck.cards)
        self.assertNotIn(c, deck.cards)
    
    def test_give_ready_deck(self):
        a = Deck.give_ready_deck()
        self.assertEqual(len(a), 52)
        self.assertIsInstance(a, Deck)
        


        


# python.exe -m unittest discover tests