# holding each players points and name
class Player:

    def __init__(self):
        self.high_score = 0  # high score for that specific player, 0 to begin with
        self.name = self.choose_name()

    # player chooses what name they want to be displayed as
    def choose_name(self):
        return input('What name do you want to display yourself as?')

    # add points to the player
    def add_points(self, points_to_add):
        self.high_score += points_to_add
