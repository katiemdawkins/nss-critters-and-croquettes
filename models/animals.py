from models.pondVillage.fish import Fish


class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()
        
pond_village = PettingZoo("Pond Village")

blue_guy = Fish("Blue Guy", "fish", "fish food")

pond_village = PettingZoo("Pond Village")
pond_village.animals.append(blue_guy)

for animal in pond_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {pond_village.attraction_name}')

