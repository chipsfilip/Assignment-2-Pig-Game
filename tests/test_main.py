#unit_test1

import unittest
from unittest.mock import patch
import main
from player import Player

class TestGameInstance(unittest.TestCase):

    @patch('main.Game')  # Mockar Game så vi inte kör play_game
    def test_game_instance_created(self, MockGame):
        """Testar att main() skapar en Game-instans med två spelare."""
        mock_game_instance = MockGame.return_value
        main.main()
        args, kwargs = MockGame.call_args
        # Kontrollera att Game skapades med två Player-objekt
        self.assertEqual(len(args[0]), 2)
        self.assertIsInstance(args[0][0], Player)
        self.assertIsInstance(args[0][1], Player)
        # Kontrollera att play_game anropades
        mock_game_instance.play_game.assert_called_once()

if __name__ == '__main__':
    unittest.main()



#unit_test2

import unittest
from unittest.mock import patch
import main

class TestPlayersCreated(unittest.TestCase):

    @patch('main.Player')
    def test_two_players_created(self, MockPlayer):
        """Testar att main() skapar två Player-objekt."""
        main.main()
        self.assertEqual(MockPlayer.call_count, 2)

if __name__ == '__main__':
    unittest.main()

