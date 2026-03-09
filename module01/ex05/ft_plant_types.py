# Plant Class
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def display_info(self):
        print (f"{self.name}: {self.height} cm {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    def bloom(self):
        print (f"{self.name} is blooming beautifully!")
    def display_info(self):
        print (f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self):
        print (f"{self.name} provides 78 square meters of shade")
    def display_info(self):
        print (f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    def display_info(self):
        print (f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")
        print (f"{self.name} is rich in {self.nutritional_value}")

print ("=== Garden Plant Types ===")
print ("\n")
rose = Flower("Rose", 25, 30, "red")
rose.display_info()
rose.bloom()
print ("\n")

oak = Tree("Oak", 500, 1825, 50)
oak.display_info()
oak.produce_shade()
print ("\n")

tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
tomato.display_info()