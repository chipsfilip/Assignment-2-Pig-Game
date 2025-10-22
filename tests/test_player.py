#unit_test1
import unittest
from unittest.mock import patch
from player import Player

class TestPlayerName(unittest.TestCase):

    @patch('builtins.input', return_value='Maryam')
    def test_choose_name(self, mock_input):
        """
        Testar att Player.choose_name() korrekt sätter spelarens namn.
        Vi mockar input så att den alltid returnerar 'Maryam'.
        """
        player = Player()
        self.assertEqual(player.name, 'Maryam')

if __name__ == '__main__':
    unittest.main()


#unit_test2

import unittest
from unittest.mock import patch
from player import Player

class TestPlayerAddPoints(unittest.TestCase):

    @patch('builtins.input', return_value='Filip')
    def test_add_points(self, mock_input):
        """
        Testar att Player.add_points() korrekt ökar spelarens high_score.
        """
        player = Player()
        player.add_points(10)
        self.assertEqual(player.high_score, 10)
        player.add_points(5)
        self.assertEqual(player.high_score, 15)

if __name__ == '__main__':
    unittest.main()
