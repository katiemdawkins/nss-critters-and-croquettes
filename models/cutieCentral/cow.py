from models.animals import Animal


class Cow(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
    
purple = Cow("Purple", "cow", "morning", "cow feed", 1234)

print(purple.chip_num)

