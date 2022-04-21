from animals.animals import Animal


class Swan(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swiming = True
    
lucy = Swan("Lucy", "swan", "swan kibble", 55)

