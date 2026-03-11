class InvalidPlant(Exception):
    pass

def water_plants(plant_list):
    try:
        print ("Opening watering system...")
        for plant in plant_list:
            if (plant == None):
                raise InvalidPlant("Cannot water None - invalid plant!")
            print ("Watering", plant)
    except InvalidPlant as e:
        print ("Error:", e)
    else:
        print ("Watering completed successfully!")
    finally:
        print ("Closing watering system (cleanup)")


def test_watering_system():
    print ("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print ("\nTesting with error...")
    water_plants(["tomato", None])
    print ("\nCleanup always happens, even with errors!")

print ("=== Garden Watering System ===\n")
test_watering_system()