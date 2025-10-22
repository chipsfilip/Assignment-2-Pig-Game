
#unit_test1

import unittest
from dice import Dice

class TestDiceMaryam(unittest.TestCase):

    def setUp(self):
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

if __name__ == '__main__':
    unittest.main()






#unit_test2

    def test_stress_roll_dice_maryam(self):
        """Maryam kör ett stresstest med många kast för att se att inget värde hamnar utanför 1–6."""
        antal_kast = 10000  #kast för att testa robustheten
        for _ in range(antal_kast):
            result = self.dice.roll_dice()
            self.assertTrue(
                1 <= result <= 6,
                f"Maryam upptäckte ett ogiltigt resultat: {result}"
            )


