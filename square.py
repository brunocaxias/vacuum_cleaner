class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dirty = True  # Assume all squares are dirty initially
        self.next_square_right = None
        self.next_square_below = None

    def is_dirty(self):
        return self.dirty
    