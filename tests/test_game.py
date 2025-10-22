#unit_tast1

import unittest
from game import Game

# En enkel mockklass för spelare
class MockPlayer:
    def __init__(self, name, high_score=0):
        self.name = name
        self.high_score = high_score

    def add_points(self, points):
        self.high_score += points


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = MockPlayer("Maryam")
        self.player2 = MockPlayer("Spelare2")
        self.game = Game([self.player1, self.player2])

    def test_current_player(self):
        """Maryam testar att current_player() fungerar korrekt."""
        current = self.game.current_player()
        self.assertEqual(current.name, "Maryam", "Första spelaren borde vara Maryam")

    def test_next_player(self):
        #Maryam testar att next_player() flyttar turen till nästa spelare.#
        self.game.next_player()
        self.assertEqual(
            self.game.current_player().name,
            "Spelare2",
            "Efter Maryam borde det vara Spelare2:s tur"
        )


if __name__ == '__main__':
    unittest.main()



#unit_tast2

import unittest
from game import Game

# Enkel mock-klass för spelare
class MockPlayer:
    def __init__(self, name, high_score=0):
        self.name = name
        self.high_score = high_score

    def add_points(self, points):
        self.high_score += points

class TestGameNew(unittest.TestCase):
    def setUp(self):
        self.maryam = MockPlayer("Maryam")
        self.hawra = MockPlayer("Hawra")
        self.game = Game([self.maryam, self.hawra])

    def test_next_player_loops_back(self):
        """Testar att next_player() loopar tillbaka till första spelaren."""
        self.game.next_player()  # tur till Hawra
        self.assertEqual(self.game.current_player().name, "Hawra")
        self.game.next_player()  # tur tillbaka till Maryam
        self.assertEqual(self.game.current_player().name, "Maryam")

    def test_has_won_false_when_no_one_reached_goal(self):
        """Testar att has_won() returnerar False när ingen nått 100 poäng."""
        self.maryam.high_score = 50
        self.hawra.high_score = 80
        self.assertFalse(self.game.has_won())

if __name__ == '__main__':
    unittest.main()

