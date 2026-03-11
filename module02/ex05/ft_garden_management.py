class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

class GardenManager:
    def __init__(self):
        self.plants = []
    def add_plant(self, plant):
        try:
                if (plant == "" or plant is None):
                    raise ValueError("Error adding plant: Plant name cannot be empty!")
                self.plants += [plant]
                print (f"Added {plant} successfully")
        except ValueError as e:
            print (e)
    def water_plants(self):
        print ("Opening watering system")
        try:
            for plant in self.plants:
                if (plant == "" or plant is None):
                    raise WaterError("Not enough water in tank")
                print ("Watering", plant, "- success")
        except GardenError as e:
            print ("Caught GardenError:", e)
        finally:
            print ("Closing watering system (cleanup)")
    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        try:
            if (plant_name == "" or plant_name is None):
                raise ValueError(f"Error checking {plant_name}: Plant name cannot be empty!")
            if (water_level < 1):
                raise ValueError(f"Error checking {plant_name}: Water level {water_level} is too low (min 1)")
            elif (water_level > 10):
                raise ValueError(f"Error checking {plant_name}: Water level {water_level} is too high (max 10)")
            if (sunlight_hours < 2):
                raise ValueError(f"Error checking {plant_name}: Sunlight hours {sunlight_hours} is too low (min 2)")
            elif (sunlight_hours > 12):
                raise ValueError(f"Error checking {plant_name}: Sunlight hours {sunlight_hours} is too high (max 12)")
        except ValueError as e:
            print (e)
        else:
            print (f"{plant_name}: healthy! (water: {water_level}, sun: {sunlight_hours})")


def test_garden_management():
    print ("=== Garden Management System ===")
    manager = GardenManager()
    print ("\nAdding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")
    
    print ("\nWatering plants...")
    manager.water_plants()

    print ("\nChecking Plant health...")
    manager.check_plant_health("tomato", 5, 8)
    manager.check_plant_health("lettuce", 15, 8)

    manager.plants = [""]
    print ("\nTesting error recovery...")
    manager.water_plants()
    print ("System recovered and continuing...")
    print ("\nGarden management system test complete!")
test_garden_management()
