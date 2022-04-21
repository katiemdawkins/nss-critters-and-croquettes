from animals.animals import Animal


class Fish(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swiming = True

  
blue_guy = Fish("Blue Guy", "fish", "fish food", 11)
print(f'{blue_guy.name} the {blue_guy.species} eats {blue_guy.food}')