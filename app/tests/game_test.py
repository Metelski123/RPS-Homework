import unittest

from app.models.game import Game 
from app.models.player import Player 

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player('Jan', "rock")
        self.player2 = Player('Jessica', 'scissors')
        self.game = Game("Jan", "Jessica")


    def test_game_output(self):
        self.assertEqual("Rock smashes scissors, Player1 wins!", self.game.rps(self.player1, self.player2))