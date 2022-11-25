import unittest

from files.card import Card


class CardTest(unittest.TestCase):
    
    def test_if_card_have_suit(self):
        card = Card(suit = "Hearts", rank =  "2")
        self.assertEqual(
            card.suit,
            "Hearts"
        )
       
    def test_if_card_have_rank(self):
        card = Card(suit = "Hearts", rank =  "2")
    
        self.assertEqual(
            card.rank,
            "2"
        )
    
    def test_if_card_knows_its_value(self):
        card = Card(suit = "Hearts", rank =  "2")
        self.assertEqual(
            card.value,
            2
        )
    def test_card_knows_how_to_add_them(self):
        card1 = Card(suit = "Hearts", rank =  "2")
        card2 = Card(suit = "Spades", rank = "Ace")
        self.assertEqual(
            card1 + card2,
            13
        )

    def test_if_cards_know_are_they_equal(self):
        card1 = Card(suit = "Hearts", rank = "2")
        card2 = Card(suit = "Hearts", rank = "2")
        self.assertEqual(
            card1,
            card2
        )

    def test_creates_all_cards(self):
        Card.create_all()
        self.assertEqual(
            len(Card.ALL_CARDS),
            52
        )
        self.assertIsInstance(
            Card.ALL_CARDS[-1],
            Card
        )



# python.exe -m unittest discover tests