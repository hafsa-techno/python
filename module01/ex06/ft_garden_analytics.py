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
    def display_info(self):
        print (f"{self.name}: {self.height}cm, {self.color} flowers ({'blooming' if self.blooming else 'not blooming'})")

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, blooming, prize_points):
        super().__init__(name, height, color, blooming)
        self.prize_points = prize_points
    def get_type(self):
        return "prize"
    def get_info(self):
        return (f"{self.name}: {self.height}cm, {self.color} flowers ({'blooming' if self.blooming else 'not blooming'}), Prize points: {self.prize_points}")
    
class Garden:

    def __init__(self, owner_name, plants):
        self.owner_name = owner_name
        self.plants = plants
        self.total_added = 0
        self.total_growth = 0
        self.regular = 0
        self.flowering = 0
        self.prize = 0
    # add plant
    def add_plant(self, plant):
        self.plants += [plant]
        self.total_added += 1
        print (f"Added {plant.name} to {self.owner_name}'s garden")
    # grow all plants
    def grow_all_plants(self):
        print (f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            print (f"{plant.name} grew 1cm")
            self.total_growth += 1
    # report
    def report(self):
        print (f"=== {self.owner_name}'s Garden Report ===")
        print ("Plants in garden:")
        for plant in self.plants:
            print (" -", plant.get_info())
            plant_type = plant.get_type()
            if (plant_type == "regular"):
                self.regular += 1
            elif (plant_type == "flowering"):
                self.flowering += 1
            else:
                self.prize += 1
        print (f"Plants added: {self.total_added}, Total growth: {self.total_growth}cm")
        print (f"Plant types: {self.regular} regular, {self.flowering} flowering, {self.prize} prize flowers")

print ("=== Garden Management System Demo ===")
oak = Plant("Oak Tree", 101)
rose = FloweringPlant("Rose", 26, "red", True)
sunflower = PrizeFlower("Sunflower", 51, "yellow", True, 10)

print ("\n")
alice_garden = Garden("Alice", [])
alice_garden.add_plant(oak)
alice_garden.add_plant(rose)
alice_garden.add_plant(sunflower)

print ("\n")
alice_garden.grow_all_plants()
print ("\n")
alice_garden.report()

print (sunflower.get_info())
