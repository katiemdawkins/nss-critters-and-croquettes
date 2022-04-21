from animals.animals import Animal


class Turtle(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swiming = True  
    
freddy = Turtle("Freddy", "turtle", "flies", 66)

