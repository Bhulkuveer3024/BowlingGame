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
        self.assert_score(0)

    def test_all_ones(self):
        """Test a game where each roll knocks down 1 pin."""
        self.roll_many(20, 1)
        self.assert_score(20)

    def test_one_spare(self):
        """Test a game with one spare."""
        self.roll_spare(5, 3)
        self.assert_score(16)

    def test_one_strike(self):
        """Test a game with one strike."""
        self.roll_strike(3, 4)
        self.assert_score(24)

    def test_perfect_game(self):
        """Test a perfect game (all strikes)."""
        self.roll_many(10, 10)  # 10 strikes for the first 10 frames
        self.roll_many(2, 10)  # Bonus rolls
        self.assert_score(300)

    def test_all_spares(self):
        """Test a game where every frame is a spare."""
        self.roll_many(21, 5)  # 10 frames of 5-5 spares + 1 bonus roll
        self.assert_score(150)

    def test_mixed_game(self):
        """Test a game with a mix of strikes, spares, and open frames."""
        self.game.roll(10)  # Strike
        self.roll_spare(5, 3)  # Spare
        self.game.roll(4)  # Open frame
        self.roll_many(14, 0)  # Remaining rolls
        self.assert_score(43)

    def test_tenth_frame_spare(self):
        """Test a game with a spare in the last frame."""
        self.roll_many(18, 0)  # 18 rolls of 0
        self.roll_spare(5, 3)  # Spare in the last frame
        self.assert_score(13)

    def test_tenth_frame_strike(self):
        """Test a game with a strike in the last frame."""
        self.roll_many(18, 0)  # 18 rolls of 0
        self.roll_strike(3, 4)  # Strike in the last frame
        self.assert_score(24)

    def test_invalid_roll(self):
        """Test that an invalid roll raises a ValueError."""
        with self.assertRaises(ValueError):
            self.game.roll(11)  # Invalid roll

    def test_exceeding_pins_in_frame(self):
        """Test that exceeding pins in a frame raises a ValueError."""
        self.game.roll(5)
        with self.assertRaises(ValueError):
            self.game.roll(6)  # Invalid second roll in the frame

    def assert_score(self, expected_score):
        """Helper to assert the score of the game."""
        self.assertEqual(expected_score, self.game.score())

    def roll_spare(self, first_roll, bonus_roll):
        """Helper to roll a spare."""
        self.game.roll(first_roll)
        self.game.roll(10 - first_roll)  # Second roll to make a spare
        self.game.roll(bonus_roll)

    def roll_strike(self, bonus_roll1, bonus_roll2):
        """Helper to roll a strike."""
        self.game.roll(10)  # Strike
        self.game.roll(bonus_roll1)
        self.game.roll(bonus_roll2)

if __name__ == '__main__':
    unittest.main()
