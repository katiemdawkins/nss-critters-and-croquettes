from animals.animals import Animal


class Goldfish(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swiming = True

  
susan = Goldfish("Susan", "goldfish", "fish food", 33)

