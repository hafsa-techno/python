class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def grow(self):
        self.height = self.height + 1
    def get_type(self):
        return "regular"
    def get_info(self):
        return (f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color, blooming):
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming
    def bloom(self):
        self.blooming = True
    def get_type(self):
        return "flowering"
    def get_info(self):
        return (f"{self.name}: {self.height}cm, {self.color} flowers ({'blooming' if self.blooming else 'not blooming'})")

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, blooming, prize_points):
        super().__init__(name, height, color, blooming)
        self.prize_points = prize_points
    def get_type(self):
        return "prize"
    def get_info(self):
        return (f"{self.name}: {self.height}cm, {self.color} flowers ({'blooming' if self.blooming else 'not blooming'}), Prize points: {self.prize_points}")

class GardenManager:
    total_gardens = 0
    def __init__(self):
        self.gardens = []
    class GardenStats:
        def __init__(self):
            self.total_added = 0
            self.total_growth = 0
            self.regular = 0
            self.flowering = 0
            self.prize = 0
        def calc_stat(self, garden):
            score = 0
            for plant in garden.plants:
                score += plant.height
                if (plant.get_type() == "prize"):
                    score += plant.prize_points
            return (score)
    # add garden
    def add_garden(self, garden):
        self.gardens += [garden]
        GardenManager.total_gardens += 1
    @classmethod
    def create_garden_network(cls):
        return cls()
    @staticmethod
    def validate_height(height):
        return height >= 0

class Garden:

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        self.stats = GardenManager.GardenStats()

    # add plant
    def add_plant(self, plant):
        self.plants += [plant]
        self.stats.total_added += 1
        print (f"Added {plant.name} to {self.owner_name}'s garden")
    # grow all plants
    def grow_all_plants(self):
        print (f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            print (f"{plant.name} grew 1cm")
            self.stats.total_growth += 1
    # report
    def report(self):
        self.stats.regular = 0
        self.stats.flowering = 0
        self.stats.prize = 0
        print (f"=== {self.owner_name}'s Garden Report ===")
        print ("Plants in garden:")
        for plant in self.plants:
            print (" -", plant.get_info())
            plant_type = plant.get_type()
            if (plant_type == "regular"):
                self.stats.regular += 1
            elif (plant_type == "flowering"):
                self.stats.flowering += 1
            else:
                self.stats.prize += 1
        print (f"Plants added: {self.stats.total_added}, Total growth: {self.stats.total_growth}cm")
        print (f"Plant types: {self.stats.regular} regular, {self.stats.flowering} flowering, {self.stats.prize} prize flowers")

print ("=== Garden Management System Demo ===")
oak = Plant("Oak Tree", 101)
rose = FloweringPlant("Rose", 26, "red", True)
sunflower = PrizeFlower("Sunflower", 51, "yellow", True, 10)

print ("\n")
alice_garden = Garden("Alice")
alice_garden.add_plant(oak)
alice_garden.add_plant(rose)
alice_garden.add_plant(sunflower)

print ("\n")
alice_garden.grow_all_plants()
print ("\n")
alice_garden.report()
print ("\n")
# Bob's Garden
bob_garden = Garden("Bob")
bob_garden.add_plant(oak)
bob_garden.add_plant(rose)

print ("\n")

manager = GardenManager()

manager.add_garden(alice_garden)
manager.add_garden(bob_garden)

alice_score = alice_garden.stats.calc_stat(alice_garden)
bob_score = bob_garden.stats.calc_stat(bob_garden)
print (f"Garden Scores - Alice: {alice_score}, Bob: {bob_score}")
print ("Total gardens managed:", GardenManager.total_gardens)
