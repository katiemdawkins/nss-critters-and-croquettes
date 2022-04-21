from datetime import date
from animals.animals import Animal

class Donkey(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

mr_donkey = Donkey("Mr Donkey", "donkey", "afternoon", "grain",333) 

print(f'{mr_donkey.name} the {mr_donkey.species} eats {mr_donkey.food}')