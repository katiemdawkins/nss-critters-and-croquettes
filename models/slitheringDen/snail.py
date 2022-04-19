from datetime import date
        
class Snail:
    def __init__(self, name, species,food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
    
        
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    def __str__(self):
        return f"{self.name} is a {self.species}."     
lil_guy= Snail("Lil Guy","snail", "snail gruel")
print(lil_guy.feed())