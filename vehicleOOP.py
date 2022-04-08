class vehicle:
    def __init__(self, engine):
        self.engine = engine
        
        super().__init__(**kwargs)

class car(vehicle):
    def __init__(self, seats, mpg):
        self.seats = seats
        self.mpg = mpg
        super().__init__(**kwargs)

        
class truck(vehicle):
    def __init__(self, load, wheels):
        self.load = load
        self.wheels = wheels
        super().__init__(**kwargs)