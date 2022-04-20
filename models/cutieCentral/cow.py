from datetime import date

class Cow:

    def __init__(self, name, species, shift, food, chip_num):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
        self.__chip_num = chip_num
    
    @property #the getter
    def chip_num(self):
        return self.__chip_num
    
    @chip_num.setter
    def chip_num(self, number):
        pass
        
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    def __str__(self):
        return f"{self.name} is a {self.species}."  
    
purple = Cow("Purple", "cow", "morning", "cow feed", 1234)

print(purple.chip_num)

