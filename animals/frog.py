from animals.animals import Animal


class Frog(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swiming = True
        
froggy = Frog("Froggy", "frog", "flies", 22)

print(f'{froggy.name} the {froggy.species} eats {froggy.food}')
