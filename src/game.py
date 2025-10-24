from dice import Dice
from computer import Computer


class Game:
    """Main logic of the game"""
    def __init__(self, players):
        """Initial setup for the game"""
        self.players = players
        self.winning_goal = 100
        self.dice = Dice()
        self.computer = Computer()
        self.current_player_index = 0  # Current player's index (begins with 0)
        self.how_many_players = len(self.players)

    def current_player(self):
        """Returns the current player"""
        return self.players[self.current_player_index]

    def next_player(self):
        """Go to the next player in the list of players"""
        # If player index should exceed amount of players, go back to the
        # first player in the list
        if self.current_player_index + 1 >= self.how_many_players:
            self.current_player_index = 0
        # Otherwise increase current player index by 1
        else:
            self.current_player_index += 1

    def hold(self, turn_score):
        """Ask if the person wants to hold or continue rolling."""
        if self.current_player().is_computer:
            return self.computer.intelligence(turn_score)
        else:
            # Use built in "lower" function to convert capital Y and N
            answer = input(
                'Do you want to hold? '
                '("y" - yes, or "n" - no)'
            ).lower()

            if answer == 'y':
                return True
            elif answer == 'n':
                return False
            else:
                print('Invalid input, try again.')
                return self.hold(turn_score)  # Ask again

    def turn(self):
        """Turn logic"""
        turn_score = 0
        player = self.current_player()

        print(
            f"It's {player.name}'s turn. Their current high score is: "
            f"{player.high_score}"
        )

        while True:
            dice_value = self.dice.roll_dice()

            print(f'{player.name} rolled the dice.')

            if dice_value == 1:
                print(f"It's a 1, {player.name} lost their round points.")

                turn_score = 0
                break
            else:
                print(f"It's a {dice_value}")

                turn_score += dice_value

                print(f'The round score is: {turn_score}')

                # Ask if they want to hold
                if self.hold(turn_score):
                    player.add_points(turn_score)
                    print(
                        f'{player.name} holds. Their high score is now: '
                        f'{player.high_score}'
                    )
                    break
        self.next_player()

    def has_won(self):
        """Check if someone has won or not"""
        for player in self.players:
            if player.high_score >= self.winning_goal:
                print(
                    f'{player.name} was the first to achieve 100 points. '
                    f'{player.name} is the winner of the game. '
                    'Congratulations!'
                )
                return True
        return False

    def play_game(self):
        """Loop game until someone has won"""
        print('The game has started. Welcome to the Pig Dice game!')
        while not self.has_won():
            self.turn()
