import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from files.walet import Walet
from files.player import Player


class WaletTest(unittest.TestCase):
    def test_if_own_amount_start_with_1000(self):

        walet = Walet(1000)
        self.assertEqual(walet.own_points, 1000)

    def test_change_number_for_chips(self):
        walet=Walet(1000)

        self.assertEqual(walet.own_chips, {"Red"  : 1, "Gold" : 2, "Blue" : 2})

    def test_beted_points(self):
        walet = Walet(500)
        self.assertEqual(walet.bet_points, 0)

    def test_beted_chips(self):
        walet = Walet(500)
        self.assertEqual(walet.bet_chips, {})

    def test_raise_bet(self):
        walet = Walet(1000)
        walet.raise_bet(100)
        walet.raise_bet(100)
        self.assertEqual(walet.own_points,800)
        self.assertEqual(walet.bet_points, 200)
        self.assertEqual(walet.bet_chips, {"Green" : 1, "Blue" : 2})
        self.assertEqual(walet.own_chips, {"Red"  : 1, "Gold" : 1, "Blue" : 2 })

    def test_lose_bet(self):
        walet = Walet(1000)
        walet.raise_bet(100)
        walet.raise_bet(100)
        walet.raise_bet(100)
        walet.lose_bet()
        self.assertEqual(walet.own_points, 700)
        self.assertEqual(walet.bet_points, 0)
    
    def test_win_bet(self):
        walet = Walet(1000)
        walet.raise_bet(100)
        walet.raise_bet(100)
        walet.raise_bet(100)
        walet.win_bet()
        self.assertEqual(walet.own_points, 1300)
        self.assertEqual(walet.bet_points, 0)

    def test_walet_equality(self):
        walet1 = Walet(1000)
        walet2 = Walet(1000)
        walet3 = Walet(999)
        self.assertEqual(walet1, walet2)
        self.assertNotEqual(walet1, walet3)


    @patch('files.walet.input')
    def test_add_walet_to_player(self, mock_input):
        walet = Walet(1000)
        player = Player("player1")
        mock_input.return_value = "1000"
        ready_walet = Walet.add_walet_to_player(player)
        self.assertEqual(ready_walet.own_points, 1000)
