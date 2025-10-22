from game import Game
from player import Player


# main function creating the players + the game, and running the game
def main():
    player_one = Player()
    player_two = Player()
    game_instance = Game([player_one, player_two])
    game_instance.play_game()


if __name__ == '__main__':
    main()
