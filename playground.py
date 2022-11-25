import unittest
from unittest.mock import MagicMock

from files.game_round import GameRound
from files.card import Card
from files.deck import Deck
from files.player import Player
from files.walet import Walet


new_deck = Deck()

print(len(new_deck))