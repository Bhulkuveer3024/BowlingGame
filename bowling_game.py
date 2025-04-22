class BowlingGame:
    def __init__(self):
        self.frames = []
        self.current_frame = []

    def roll(self, pins):
        # Validate the number of pins knocked down
        if pins < 0 or pins > 10:
            raise ValueError("Invalid number of pins. Must be between 0 and 10.")
        
        if len(self.frames) < 10:  # A bowling game consists of 10 frames
            if len(self.current_frame) < 2:  # Each frame can have a maximum of 2 rolls
                if len(self.current_frame) == 0 and pins == 10:
                    # If it's a strike, we don't add a second roll
                    self.current_frame.append(pins)
                    self.frames.append(self.current_frame)
                    self.current_frame = []
                elif len(self.current_frame) == 1 and (self.current_frame[0] + pins > 10):
                    raise ValueError("Invalid second roll in the frame. Total pins cannot exceed 10.")
                else:
                    self.current_frame.append(pins)
                    if len(self.current_frame) == 2:
                        self.frames.append(self.current_frame)
                        self.current_frame = []
            else:
                raise Exception("Game is already over. No more rolls allowed.")
        elif len(self.frames) == 10:  # Handle bonus rolls after the 10th frame
            if len(self.current_frame) < 3:  # Allow up to 3 rolls in the last frame
                self.current_frame.append(pins)
                # Check if we should finalize the game
                if len(self.current_frame) == 3 or (len(self.current_frame) == 2 and self.is_strike(self.frames[-1])):
                    self.frames.append(self.current_frame)
                    self.current_frame = []
            else:
                raise Exception("Game is already over. No more rolls allowed.")

    def score(self):
        total_score = 0
        for i in range(len(self.frames)):
            frame = self.frames[i]
            if self.is_strike(frame):
                total_score += 10 + self.strike_bonus(i)
            elif self.is_spare(frame):
                total_score += 10 + self.spare_bonus(i)
            else:
                total_score += sum(frame)
        return total_score

    def is_strike(self, frame):
        return frame[0] == 10

    def is_spare(self, frame):
        return sum(frame) == 10 and len(frame) == 2

    def strike_bonus(self, frame_index):
        if frame_index + 1 < len(self.frames):
            next_frame = self.frames[frame_index + 1]
            if self.is_strike(next_frame):
                if frame_index + 2 < len(self.frames):
                    return 10 + self.frames[frame_index + 2][0]
                return 10  # Last frame strike bonus
            return sum(next_frame)
        return 0
       

    def spare_bonus(self, frame_index):
        if frame_index + 1 < len(self.frames):
            return self.frames[frame_index + 1][0] 
        return 0
        
