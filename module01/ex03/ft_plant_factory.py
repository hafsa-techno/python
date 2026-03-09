class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age_days = age
    def grow(self):
        self.height = self.height + 1
    def age(self):
        self.age_days = self.age_days + 1
    def get_info(self):
        return (f"{self.name}: ({self.height}cm, {self.age_days} days)")

rose = Plant("Rose", 25, 30)
oak = Plant("Oak", 200, 365)
cactus = Plant("Cactus", 5, 90)
sunflower = Plant("Sunflower", 80, 45)
fern = Plant("Fern", 15, 120)

plants = [
    rose,
    oak,
    cactus,
    sunflower,
    fern
]

print ("=== Plant Factory Output ===")
count = 0
for plant in plants:
    print (f"Created: {plant.get_info()}")
    count += 1
print ("\nTotal plants created:", count)