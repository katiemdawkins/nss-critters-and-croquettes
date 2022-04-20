from animals import Animal

# Designate Llama as a child class by adding (Animal) after the class name

class Llama(Animal):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift # stays on Llama because not all animals have shifts
        self.walking = True
         
miss_fuzz = Llama("Miss Fuzz", "Llama", "midday", "llama chow")

print(f'{miss_fuzz.name} is a {miss_fuzz.species}')