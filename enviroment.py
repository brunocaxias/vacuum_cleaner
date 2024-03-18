class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.squares = [[Square(x, y) for y in range(height)] for x in range(width)]
        self.populate_next_squares()

    def populate_next_squares(self):
        for x in range(self.width):
            for y in range(self.height):
                square = self.squares[x][y]
                if x < self.width - 1:
                    square.next_square_right = self.squares[x + 1][y]
                if y < self.height - 1:
                    square.next_square_below = self.squares[x][y + 1]

    def get_square(self, x, y):
        return self.squares[x][y]

    def print_status(self):
        for row in self.squares:
            for square in row:
                status = "dirty" if square.is_dirty() else "clean"
                print(f"Square at position ({square.x}, {square.y}) is {status}.")
                print(f"Next square to the right: ({square.next_square_right.x}, {square.next_square_right.y})" if square.next_square_right else "Next square to the right: None")
                print(f"Next square below: ({square.next_square_below.x}, {square.next_square_below.y})" if square.next_square_below else "Next square below: None")
                print()