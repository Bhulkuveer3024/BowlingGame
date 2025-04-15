# Bowling Game Project

This repository contains the code for a 10-pin Bowling Game scoring system. The implementation is a backend without a GUI, designed as a prototype for an educational software system.

## Project Files

- `bowling_game.py`: Contains the `BowlingGame` class that implements the scoring logic
- `example_usage.py`: Demonstrates how to use the `BowlingGame` class
- `test_bowling.py`: Basic unit tests for the `BowlingGame` class

## Game Rules

Each game of bowling consists of ten frames. In each frame, the bowler will have two chances to knock down as many pins as possible with their bowling ball.

### Scoring

- **Open Frame**: When a player fails to knock down all ten pins in a frame, they score the number of pins knocked down.
- **Spare**: When a player knocks down all ten pins using both balls of a frame, it is a spare. The player scores 10 plus the pins knocked down by the next roll.
- **Strike**: When a player knocks down all ten pins on the first roll, it is a strike. The player scores 10 plus the pins knocked down in the next two rolls.
- **10th Frame**: If the player rolls a strike or spare in the 10th frame, they get bonus rolls. The player can roll up to three balls in the 10th frame.

### Maximum Score

A perfect game (12 strikes in a row) scores 300 points.

## Task

This code is provided as a starting point for students to:

1. Create a test plan
2. Design and implement a suite of unit tests
3. Debug the application and fix any issues
4. Refactor the code to improve its quality
5. Document the code using PythonDoc
6. Use Git for version control

The code intentionally contains bugs and areas for improvement, which students are expected to identify and fix.