class BowlingGame:
    def __init__(self):
        self.frames = []
        self.current_frame = []

    def roll(self, pins):
        self.validate_pins(pins)
        if len(self.frames) < 10:
            self.handle_regular_frame(pins)
        else:
            self.handle_bonus_rolls(pins)

    def validate_pins(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Invalid number of pins. Must be between 0 and 10.")

    def handle_regular_frame(self, pins):
        if len(self.current_frame) == 0 and pins == 10:
            self.add_strike_frame(pins)
        elif len(self.current_frame) == 1 and (self.current_frame[0] + pins > 10):
            raise ValueError("Invalid second roll in the frame. Total pins cannot exceed 10.")
        else:
            self.current_frame.append(pins)
            if len(self.current_frame) == 2:
                self.frames.append(self.current_frame)
                self.current_frame = []

    def add_strike_frame(self, pins):
        self.current_frame.append(pins)
        self.frames.append(self.current_frame)
        self.current_frame = []

    def handle_bonus_rolls(self, pins):
        if len(self.current_frame) < 3:
            self.current_frame.append(pins)
            if self.should_finalize_game():
                self.frames.append(self.current_frame)
                self.current_frame = []
        else:
            raise Exception("Game is already over. No more rolls allowed.")

    def should_finalize_game(self):
        return (len(self.current_frame) == 3 or 
                (len(self.current_frame) == 2 and self.is_strike(self.frames[-1])))

    def score(self):
        total_score = 0
        for i in range(len(self.frames)):
            frame = self.frames[i]
            total_score += self.calculate_frame_score(frame, i)
        return total_score

    def calculate_frame_score(self, frame, index):
        if self.is_strike(frame):
            return 10 + self.strike_bonus(index)
        elif self.is_spare(frame):
            return 10 + self.spare_bonus(index)
        return sum(frame)

    def is_strike(self, frame):
        return frame[0] == 10

    def is_spare(self, frame):
        return sum(frame) == 10 and len(frame) == 2

    def strike_bonus(self, frame_index):
        if frame_index + 1 < len(self.frames):
            next_frame = self.frames[frame_index + 1]
            if self.is_strike(next_frame):
                return 10 + (self.frames[frame_index + 2][0] if frame_index + 2 < len(self.frames) else 0)
            return sum(next_frame)
        return 0

    def spare_bonus(self, frame_index):
        return self.frames[frame_index + 1][0] if frame_index + 1 < len(self.frames) else 0
