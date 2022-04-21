from animals.animals import Animal


class Lizard(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
      
green_guy = Lizard("Green Guy","lil lizard", "flies", 999)

print(f'{green_guy.name} the {green_guy.species} eats {green_guy.food}')