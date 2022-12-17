class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fishes":
            self.fishes.append(name)
        elif species == "birds":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fishes":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "birds":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())
for i in range(n):
    animal_info = input().split()
    species = animal_info[0]
    animal_name = animal_info[1]
    zoo.add_animal(species, animal_name)

animal_species = input()
print(zoo.get_info(animal_species))
