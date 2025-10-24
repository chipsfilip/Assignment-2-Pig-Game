# holding each players points and name
class Player:

    def __init__(self):
        self.high_score = 0  # player's high score (begins with 0)
        self.is_computer = self.ask_if_computer()  # player type (computer)
        if self.is_computer:
            self.name = 'Computer'
        else:
            self.name = self.choose_name()

    # ask if player is computer or person
    def ask_if_computer(self):
        # use built in "lower" function to convert capital C and P
        player_type = input(
            'Do you want this player to be a computer or a person? '
            '"c" - computer, or "p" - person'
        ).lower()
        if player_type == 'c':
            return True
        elif player_type == 'p':
            return False
        else:
            print('Invalid input. Please try again!')
            return self.ask_if_computer()

    # player chooses what name they want to be displayed as
    def choose_name(self):
        return input('What name do you want to display yourself as?')

    # add points to the player
    def add_points(self, points_to_add):
        self.high_score += points_to_add
