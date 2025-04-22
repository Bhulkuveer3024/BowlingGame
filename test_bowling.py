import unittest
from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        """Set up a new game before each test."""
        self.game = BowlingGame()

    def roll_many(self, n, pins):
        """Helper to roll the same number of pins multiple times."""
        for _ in range(n):
            self.game.roll(pins)

    def test_gutter_game(self):
        """Test a game where no pins are knocked down."""
        self.roll_many(20, 0)
        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        """Test a game where each roll knocks down 1 pin."""
        self.roll_many(20, 1)
        self.assertEqual(20, self.game.score())

    def test_one_spare(self):
        """Test a game with one spare."""
        self.game.roll(5)
        self.game.roll(5)  # Spare
        self.game.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(16, self.game.score())

    def test_one_strike(self):
        """Test a game with one strike."""
        self.game.roll(10)  # Strike
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(24, self.game.score())

    def test_perfect_game(self):
        """Test a perfect game (all strikes)."""
        self.roll_many(10, 10)  # 10 strikes for the first 10 frames
        self .game.roll(10)  # Bonus roll 1
        self.game.roll(10)  # Bonus roll 2
        self.assertEqual(300, self.game.score())
        
    def test_all_spares(self):
        """Test a game where every frame is a spare."""
        self.roll_many(21, 5)  # 10 frames of 5-5 spares + 1 bonus roll
        self.assertEqual(150, self.game.score())  # Each spare gives 10 + 5 bonus

    def test_mixed_game(self):
        """Test a game with a mix of strikes, spares, and open frames."""
        self.game.roll(10)  # Strike
        self.game.roll(5)
        self.game.roll(4)  # Spare
        self.game.roll(3)
        self.game.roll(4)  # Open frame
        self.roll_many(14, 0)  # Remaining rolls
        self.assertEqual(43, self.game.score())  # Calculate the score based on the rolls

    def test_tenth_frame_spare(self):
        """Test a game with a spare in the last frame."""
        self.roll_many(18, 0)  # 18 rolls of 0
        self.game.roll(5)
        self.game.roll(5)  # Spare in the last frame
        self.game.roll(3)  # Bonus roll
        self.assertEqual(13, self.game.score())  # 5 + 5 + 3 = 13

    def test_tenth_frame_strike(self):
        """Test a game with a strike in the last frame."""
        self.roll_many(18, 0)  # 18 rolls of 0
        self.game.roll(10)  # Strike in the last frame
        self.game.roll(3)
        self.game.roll(4)  # Bonus rolls
        self.assertEqual(24, self.game.score())  # 10 + (3 + 4) + 3 + 4 = 24

    def test_invalid_roll(self):
        """Test that an invalid roll raises a ValueError."""
        with self.assertRaises(ValueError):
            self.game.roll(11)  # Invalid roll

    def test_exceeding_pins_in_frame(self):
        """Test that exceeding pins in a frame raises a ValueError."""
        self.game.roll(5)
        with self.assertRaises(ValueError):
            self.game.roll(6)  # Invalid second roll in the frame

if __name__ == '__main__':
    unittest.main()
