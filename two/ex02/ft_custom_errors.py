class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass


def check_plant():
    raise PlantError("The tomato plant is wilting!\n")

def check_water():
    raise WaterError("Not enough water in the tank!\n")

print ("=== Custom Garden Errors Demo ===\n")

try:
    print ("Testing PlantError...")
    check_plant()
except PlantError as e:
    print ("Caught PlantError:", e)

try:
    print ("Testing WaterError...")
    check_water()
except WaterError as e:
    print ("Caught WaterError:", e)


print ("Testing catching all garden errors...")
try:
    check_plant()
except GardenError as e:
    print ("Caught a garden error:", e)

try:
    check_water()
except GardenError as e:
    print ("Caught a garden error:", e)
print ("All custom error types work correctly!")