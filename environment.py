import square

class Enviroment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.squares = [[square.Square(x, y) for y in range(height)] for x in range(width)] # Matriz de quadrados

    def get_square(self, x, y):
        return self.squares[x][y]

    def print_status(self):
        for row in self.squares:
            for square in row:
                status = "sujo" if square.is_dirty() else "limpo"
                print(f"Quadrado na posição ({square.x}, {square.y}) está {status}.")
                print()