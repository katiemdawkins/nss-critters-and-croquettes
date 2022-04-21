from attractions.attractions import PettingZoo, SnakePit, Wetlands
from animals.cow import Cow
from animals.donkey import Donkey
from animals.goat import Goat
from animals.hamster import Hamster
from animals.llama import Llama
from animals.pig import Pig
from animals.fish import Fish
from animals.frog import Frog
from animals.goldfish import Goldfish
from animals.mallard import Mallard
from animals.swan import Swan
from animals.turtle import Turtle
from animals.lizard import Lizard
from animals.snail import Snail
from animals.snake import Snake

#------------------------------------------Pond Village----------------------
pond_village = Wetlands("Pond Village")

blue_guy = Fish("Blue Guy", "fish", "fish food", 11)

froggy = Frog("Froggy", "frog", "flies", 22)

susan = Goldfish("Susan", "goldfish", "fish food", 33)

larry = Mallard("Larry", "duck", "duck foodz", 44)

lucy = Swan("Lucy", "swan", "swan kibble", 55)

freddy = Turtle("Freddy", "turtle", "flies", 66)

pond_village.add_animal(blue_guy)
pond_village.add_animal(froggy)
pond_village.add_animal(susan)
pond_village.add_animal(larry)
pond_village.add_animal(freddy)

print(f'{pond_village.attraction_name} is where you can find {pond_village.description}, like')
for animal in pond_village.animals:
    print(f'* {animal.name} the {animal.species}')
#------------------------------------------Slither Inn----------------------
slither_inn = SnakePit("Slither Inn")

green_guy = Lizard("Green Guy","lil lizard", "flies", 999)
lil_guy= Snail("Lil Guy","snail", "snail gruel", 777)
snakey= Snake("Snakey", "copperhead", "rats", 888)

slither_inn.add_animal(green_guy)
slither_inn.add_animal(lil_guy)
slither_inn.add_animal(snakey)
print(f'{slither_inn.last_critter_added}')

print(f'{slither_inn.attraction_name} is where you can find {slither_inn.description}, like') 
for animal in slither_inn.animals:
    print(f'*{animal.name} the {animal.species}')
    
#------------------------------------------Petting Zoo----------------------
critter_city = PettingZoo("Critter City")

purple = Cow("Purple", "cow", "morning", "cow feed", 1234)
mr_donkey = Donkey("Mr Donkey", "donkey", "afternoon", "grain", 333) 
lil_lady = Goat("Lil Lady", "goat", "midday", "goat feed", 222)
lionel = Hamster("Lionel", "hamster", "midday", "hamster kibble bits", 4444)
miss_fuzz = Llama("Miss Fuzz", "Llama", "midday", "llama chow", 1235)
mizz_piggy= Pig("Mizz Piggy", "pig", "morning", "slop", 555)

critter_city.add_animal(purple)
critter_city.add_animal(mr_donkey)
critter_city.add_animal(lil_lady)
critter_city.add_animal(lionel)
critter_city.add_animal(miss_fuzz)
critter_city.add_animal(mizz_piggy)
    
print(f'{critter_city.attraction_name} is where you can find {critter_city.description}, like')
for animal in critter_city.animals: 
    print(f'*{animal.name} the {animal.species}')