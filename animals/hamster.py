from animals.animals import Animal


class Hamster(Animal):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift # stays on Llama because not all animals have shifts
        self.walking = True
        
lionel = Hamster("Lionel", "hamster", "midday", "hamster kibble bits", 4444)

print(f'Alright, {lionel.name} is a {lionel.species}')