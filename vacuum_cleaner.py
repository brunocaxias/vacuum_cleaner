import environment

class VacuumCleaner:
    def __init__(self, x, y, energy=0):
        self.x = x
        self.y = y
        self.energy = energy
        self.environment_size = (0, 0)

    def clean(self, current_square):
        if current_square.is_dirty():
            current_square.clean()
            self.energy += 10
            print("Square %i , %i was cleaned" % (self.x, self.y))

    def map(self, environment):
        self.environment_size = (environment.width, environment.height)

    def move(self,x,y):
        self.x = x
        self.y = y
        self.energy += 5

    def start_cleanup(self, environment):
        self.map(environment)
        for x in range(self.environment_size[0]):
            for y in range(self.environment_size[1]):
                self.move(x, y)
                self.clean(environment.get_square(x,y))
        print("Finished cleanup")
        print()


