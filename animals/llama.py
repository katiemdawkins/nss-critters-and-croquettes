# Designate Llama as a child class by adding (Animal) after the class name
from animals.animals import Animal
from datetime import date


class Llama(Animal):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift # stays on Llama because not all animals have shifts
        self.walking = True
    def feed(self):
        print(f'{self.name} was sung to while fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

miss_fuzz = Llama("Miss Fuzz", "Llama", "midday", "llama chow", 1235)

print(f'{miss_fuzz.feed()} {miss_fuzz.name} is a {miss_fuzz.species}')
