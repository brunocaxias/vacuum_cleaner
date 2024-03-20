class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dirty = True  # Todos os quadrados estão sujos inicialmente

    def is_dirty(self):
        return self.dirty
    
    def clean(self):
        self.dirty = False
        