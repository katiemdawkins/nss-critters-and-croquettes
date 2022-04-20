from attractions import PettingZoo, SnakePit, Wetlands
from models.cutieCentral.cow import Cow
from models.cutieCentral.donkey import Donkey
from models.cutieCentral.goat import Goat
from models.cutieCentral.hamster import Hamster
from models.cutieCentral.llama import Llama
from models.cutieCentral.pig import Pig
from models.pondVillage.fish import Fish
from models.pondVillage.frog import Frog
from models.pondVillage.goldfish import Goldfish
from models.pondVillage.mallard import Mallard
from models.pondVillage.swan import Swan
from models.pondVillage.turtle import Turtle
from models.slitheringDen.lizard import Lizard
from models.slitheringDen.snail import Snail
from models.slitheringDen.snake import Snake

#------------------------------------------Pond Village----------------------
pond_village = Wetlands("Pond Village")

blue_guy = Fish("Blue Guy", "fish", "fish food")
pond_village.animals.append(blue_guy)

froggy = Frog("Froggy", "frog", "flies")
pond_village.animals.append(froggy)

susan = Goldfish("Susan", "goldfish", "fish food")
pond_village.animals.append(susan)

larry = Mallard("Larry", "duck", "duck foodz")
pond_village.animals.append(larry)

lucy = Swan("Lucy", "swan", "swan kibble")
pond_village.animals.append(lucy)

freddy = Turtle("Freddy", "turtle", "flies")
pond_village.animals.append(freddy)

for animal in pond_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {pond_village.attraction_name}')
    
#------------------------------------------Slither Inn----------------------
slither_inn = SnakePit("Slither Inn")

green_guy = Lizard("Green Guy","lil lizard", "flies")
lil_guy= Snail("Lil Guy","snail", "snail gruel")
snakey= Snake("Snakey", "copperhead", "rats")

slither_inn.add_animal(green_guy)
slither_inn.add_animal(lil_guy)
slither_inn.add_animal(snakey)

for animal in slither_inn.animals:
    print(f'You can find {animal.name} the {animal.species} in {slither_inn.attraction_name}')

#------------------------------------------Petting Zoo----------------------
critter_city = PettingZoo("Critter City")

purple = Cow("Purple", "cow", "morning", "cow feed")
mr_donkey = Donkey("Mr Donkey", "donkey", "afternoon", "grain") 
lil_lady = Goat("Lil Lady", "goat", "midday", "goat feed")
lionel = Hamster("Lionel", "hamster", "hamster kibble bits")
miss_fuzz = Llama("Miss Fuzz", "Llama", "midday", "llama chow")
mizz_piggy= Pig("Mizz Piggy", "pig", "morning", "slop")

critter_city.add_animal(purple)
critter_city.add_animal(mr_donkey)
critter_city.add_animal(lil_lady)
critter_city.add_animal(lionel)
critter_city.add_animal(miss_fuzz)
critter_city.add_animal(mizz_piggy)

for animal in critter_city.animals:
    print(f'You can find {animal.name} the {animal.species} in {critter_city.attraction_name}')