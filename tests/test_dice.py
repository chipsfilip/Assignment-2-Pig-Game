import unittest
from dice import Dice

class TestDice(unittest.TestCase):

    def setUp(self):
        # Här kan vi låtsas att Maryam testar tärningen
        self.testare = "Maryam"
        self.dice = Dice()

    def test_roll_dice_range(self):
        """Maryam testar att tärningen ger ett tal mellan 1 och 6."""
        for _ in range(100):
            result = self.dice.roll_dice()
            self.assertIn(
                result,
                range(1, 7),
                f"{self.testare} fick {result}, vilket inte är mellan 1 och 6."
            )

    def test_roll_dice_type(self):
        """Hawra kontrollerar att resultatet är ett heltal."""
        testare = "Hawra"
        result = self.dice.roll_dice()
        self.assertIsInstance(
            result,
            int,
            f"{testare} upptäckte att resultatet inte var ett heltal."
        )

    def test_multiple_rolls_filip(self):
        """Filip testar flera kast för att säkerställa slumpen."""
        testare = "Filip"
        results = [self.dice.roll_dice() for _ in range(10)]
        # Testar att alla resultat är giltiga
        for r in results:
            self.assertIn(
                r,
                range(1, 7),
                f"{testare} fick ogiltigt resultat: {r}"
            )
        # Testar att vi inte får exakt samma tal alla gånger (inte krav men bra test)
        self.assertGreater(
            len(set(results)),
            1,
            f"{testare} fick samma resultat varje gång, vilket verkar misstänkt."
        )

if __name__ == '__main__':
    unittest.main()
