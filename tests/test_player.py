
# holding each players points and name
class Player:

    def __init__(self, name):
        self.high_score = 0 # high score for that specific player, 0 to begin with
        self.name = name

    # add points to the player
    def add_points(self, points_to_add):
        self.high_score += points_to_add
