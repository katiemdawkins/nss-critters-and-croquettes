
from smtplib import SMTPRecipientsRefused
from unicodedata import name


class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "zen critters of the wetlands to chill with"
        self.animals = list()
        

class SnakePit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "slithering doodads and doodaas to view"
        self.animals = list()
        
    def add_animal(self, new_animal):
        self.animals.append(new_animal)
    
    @property #getter
    def last_critter_added(self):
        return self.animals[-1]
        
class PettingZoo:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals =list()
        
    def add_animal(self, new_animal):
        self.animals.append(new_animal)