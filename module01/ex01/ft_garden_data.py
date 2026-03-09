class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def display_info(self):
        print (f"{self.name}: {self.height} cm {self.age} days old")

def main():
    P1 = Plant("Rose", 25, 30)
    P2 = Plant("Sunflower", 80, 45)
    P3 = Plant("Cactus", 15, 120)
    print ("=== Garden Plant Registry ===")
    P1.display_info()
    P2.display_info()
    P3.display_info()

if __name__ == "__main__":
    main()