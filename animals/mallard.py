from animals.animals import Animal


class Mallard(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swiming = True   

larry = Mallard("Larry", "duck", "duck foodz", 44)

