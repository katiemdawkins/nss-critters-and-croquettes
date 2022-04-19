from datetime import date

from models.animals import PettingZoo

class Frog:

    def __init__(self, name, species, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
    
        
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}." 
        
froggy = Frog("Froggy", "frog", "flies")

pond_village = PettingZoo("Pond Village")
pond_village.animals.append(froggy)
