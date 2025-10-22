from dice import Dice


# logic of the game
class Game:

    def __init__(self, players):
        self.players = players
        self.winning_goal = 100
        self.dice = Dice()
        self.current_player_index = 0  # current player's index (begins with 0)
        self.how_many_players = len(self.players)

    # returns the current player
    def current_player(self):
        return self.players[self.current_player_index]

    # go to the next player in the list of players
    def next_player(self):
        # if player index should exceed amount of players, go back to the
        # first player in the list
        if self.current_player_index + 1 >= self.how_many_players:
            self.current_player_index = 0
        # otherwise increase current player index by 1
        else:
            self.current_player_index += 1

    # ask if the person wants to hold or continue rolling, return yes or no
    def hold(self):
        # use built in "lower" function to convert capital Y and N
        answer = input('Do you want to hold? ("y" - yes, or "n" - no)').lower()

        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print('Invalid input, try again.')
            return self.hold()  # ask again

    # do roll_dice function and add return value 2-6 to variable turn_score
    # it it returns 1, make turn_score = 0
    # add dice value to turn_score
    # ask if they want to try again, if yes -> roll dice again,
    # if not -> add turn score to high score
    def turn(self):
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
                print("It's a 1, you lose your round points.")

                turn_score = 0
                break
            else:
                print(f"It's a {dice_value}")

                turn_score += dice_value

                print(f'The round score is: {turn_score}')

                # ask if they want to hold
                if self.hold():
                    player.add_points(turn_score)
                    print(
                        f'{player.name} holds. Their high score is now: '
                        f'{player.high_score}'
                    )
                    break

        self.next_player()

    # tallying of all peoples high score and checking 
    # if someone has won or not
    def has_won(self):
        for player in self.players:
            if player.high_score >= self.winning_goal:
                print(
                    f'{player.name} was the first to achieve 100 points. '
                    f'{player.name} is the winner of the game. Congratulations!'
                )
                return True

        return False

    # game loop
    def play_game(self):
        print('The game has started. Welcome to the Pig Dice game!')
        while not self.has_won():
            self.turn()
