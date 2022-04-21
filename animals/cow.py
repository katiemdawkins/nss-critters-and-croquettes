from animals.animals import Animal
from datetime import date

class Cow(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
    def feed(self):
        print(f'{self.name}, the {self.species} was sprayed with water while fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
        
purple = Cow("Purple", "cow", "morning", "cow feed", 1234)

print(f'{purple.feed()}')

