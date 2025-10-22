import random

# holding dice-throw
class Dice:

    # roll dice between 1-6, return number
    def roll_dice(self):
        return random.randint(1, 6)
