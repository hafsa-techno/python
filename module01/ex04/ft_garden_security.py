class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)
    def set_height(self, height):
        if (height < 0):
            print (f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print (f"Height updated: {self.__height}cm [OK]")
    def get_height(self):
        return (self.__height)
    def set_age(self, age):
        if (age < 0):
            print (f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print (f"Age updated: {self.__age} days [OK]")
    def get_age(self):
        return (self.__age)
    def get_info(self):
        return (f"{self.name} ({self.__height}cm, {self.__age} days)")

print ("=== Garden Security System ===")

plant1 = SecurePlant("Rose", 25, 30)
print ("\n")
plant1.set_height(-5)
print ("\n")

print (f"Current plant: {plant1.get_info()}")