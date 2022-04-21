from animals.animals import Animal
from datetime import date
class Snail(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
    def feed(self):
        print(f'{self.name}, the {self.species} was misted with water while fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

lil_guy= Snail("Lil Guy","snail", "snail gruel", 777)

print(f'{lil_guy.feed()}')