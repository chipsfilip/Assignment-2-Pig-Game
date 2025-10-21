from game import Game
from player import Player

# main function creating the players + the game, and running the game
def main():
    player_one = Player('Player 1')
    player_two = Player('Player 2')
    game_instance = Game([player_one, player_two])
    game_instance.play_game()

if __name__ == '__main__':
    main()