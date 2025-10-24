import random


class Dice:
    """Dice-throw class"""
    def roll_dice(self):
        """Roll dice between 1-6, return number"""
        return random.randint(1, 6)
