from datetime import date
from animals.animals import Animal

class Pig(Animal):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift # stays on Llama because not all animals have shifts
        self.walking = True
  
mizz_piggy= Pig("Mizz Piggy", "pig", "morning", "slop", 555)

print(f'Yo! {mizz_piggy.name} is a {mizz_piggy.species}')