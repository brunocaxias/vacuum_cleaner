class VacuumCleaner:
    def __init__(self, x, y, energy=0):
        self.x = x
        self.y = y
        self.energy = energy
        self.environment_matrix = None

    def move_to_next_square(self, environment):
        current_square = environment.get_square(self.x, self.y)
        while current_square.next_square_right:
            self.x += 1
            current_square = current_square.next_square_right
        if current_square.next_square_below:
            self.y += 1
            self.x = 0
            current_square = current_square.next_square_below
    
    def clean(self, environment):
        current_square = environment.get_square(self.x, self.y)
        if current_square.is_dirty():
            current_square.clean()
            self.energy += 10

    def verify_if_square_is_dirty(self, environment):
        current_square = environment.get_square(self.x, self.y)
        if current_square.is_dirty():
            print("Square is dirty.")
        else:
            print("Square is clean.")

    