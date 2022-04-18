# import the python datetime module to help us create a timestamp
from datetime import date
import turtle

class Llama:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        
miss_fuzz = Llama("Miss Fuzz", "Llama")

class Donkey:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

mr_donkey = Donkey("Mr Donkey", "donkey") 
      
class Goat:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

lil_lady = Goat("Lil Lady", "goat")

class Cow:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
purple = Cow("Purple", "cow")

class Pig:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        
mizz_piggy= Pig("Mizz Piggy", "pig")

class Snake:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

snakey= Snake ("Snakey", "copperhead")

class Frog:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        
froggy = Frog("Froggy", "frog")

class Fish:
    
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
blue_guy = Fish("Blue Guy", "fish")

class Hamster:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

lionel = Hamster("Lionel", "hamster")

class Lizard:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        
green_guy = Lizard("Green Guy","lil lizard")


class Mallard:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        
larry = Mallard("Larry", "duck")
        
class Goldfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        
susan = Goldfish("Susan", "goldfish")
        
class Swan:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
lucy= Swan("Lucy", "swan")
        
class Snail:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
lil_guy= Snail("Lil Guy","snail")

class Turtle:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
freddy = Turtle("Freddy", "turtle")