import unittest

from app.models.player import Player 
from app.models.game import Game 

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Amy", "rock")
        self.player2 = Player("Bob", "scissors")


    def test_check_player1_name(self):
        self.assertEqual("Amy", self.player1.name)


    def test_check_player2_name(self):
        self.assertEqual("Bob", self.player2.name)


    def test_check_player1_choice(self):
        self.assertEqual("rock", self.player1.choice)


    def test_check_player2_choice(self):
        self.assertEqual("scissors", self.player2.choice)