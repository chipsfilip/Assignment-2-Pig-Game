from game import Game
from player import Player


def main():
    """Main function creating the players + the game, and running the game"""
    player_one = Player()
    player_two = Player()
    game_instance = Game([player_one, player_two])
    game_instance.play_game()


if __name__ == '__main__':
    main()
