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
        return (f"{self.name}: {self.height}cm, {self.age_days} days old")

rose = Plant("Rose", 25, 30)
print("=== Day 1 ===")
print (rose.get_info())
start_height = rose.height

for i in range(6):
    rose.grow()
    rose.age()

print("=== Day 7 ===")
print (rose.get_info())
print (f"Growth this week: +{rose.height - start_height}cm")
