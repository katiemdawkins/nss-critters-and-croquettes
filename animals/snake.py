from animals.animals import Animal


class Snake(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
        
snakey= Snake ("Snakey", "copperhead", "rats", 888)

print(f'{snakey.name} the {snakey.species} eats {snakey.food}')