from datetime import date
from animals.animals import Animal

class Goat(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
    
lil_lady = Goat("Lil Lady", "goat", "midday", "goat feed", 222)

print(f'{lil_lady.name} the {lil_lady.species} eats {lil_lady.food}')
