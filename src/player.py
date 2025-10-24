class Player:
    """Player class"""
    def __init__(self):
        """Initial setup for player"""
        self.high_score = 0  # Player's high score (begins with 0)
        self.is_computer = self.ask_if_computer()  # Player type (computer)
        if self.is_computer:
            self.name = 'Computer'
        else:
            self.name = self.choose_name()

    def ask_if_computer(self):
        """Ask if player is computer or person"""
        # Use built in "lower" function to convert capital C and P
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

    def choose_name(self):
        """Player chooses what name they want to be displayed as"""
        return input('What name do you want to display yourself as?')

    def add_points(self, points_to_add):
        """Add points to the player"""
        self.high_score += points_to_add
