import sys

def calc_total(values):
    count = 0
    for item in values:
        count += item
    return (count)

def max_val(diction):
    max = None
    for key, value in diction.items():
        if (max is None or value > max[1]):
            max = (key, value)
    return max

def min_val(dict):
    min = None
    for key, value in dict.items():
        if (min is None or value < min[1]):
            min = (key, value)
    return min

def main():
    if (len(sys.argv) == 1):
        return
    print ("=== Inventory System Analysis ===")
    i = 1
    inventory_dict = dict()
    while (i < len(sys.argv)):
        args = sys.argv[i].split(":")
        inventory_dict[args[0]] = int (args[1])
        i += 1
    total_units = calc_total(inventory_dict.values())
    print ("Total items in inventory:", total_units)
    print ("Unique item types:", len (inventory_dict))

    print ("\n")
    print ("=== Current Inventory ===")
    for key,value in inventory_dict.items():
        percentage = value * 100 / total_units
        print (f"{key}: {value} {'unit' if value == 1 else 'units' } ({percentage:.2f}%)")

    print ("\n=== Inventory Statistics ===")
    max_nbr = max_val(inventory_dict)
    min_nbr = min_val(inventory_dict)
    print (f"Most abundant: {max_nbr[0]} ({max_nbr[1]} {'unit' if max_nbr[1] == 1 else 'units' })")
    print (f"Least abundant: {min_nbr[0]} ({min_nbr[1]} {'unit' if min_nbr[1] == 1 else 'units' })")

    print ("\n=== Management Suggestions ===")
    print ("Restock needed: ", end="")
    restock = []
    for key, value in inventory_dict.items():
        if (value == 1):
            restock += [key]
    i = 0
    for value in restock:
        print (value, end="")
        if (i != len(restock) - 1):
            print (", ", end="")
        i += 1

    print ("\n=== Item Categories ===")
    categories = {
        "Moderate" : {},
        "Scarce": {}
    }
    for key, value in inventory_dict.items():
        if (value >= 5):
            categories["Moderate"][key] = value
        else:
            categories["Scarce"][key] = value
    print (f"Moderate: {categories['Moderate']}")
    print (f"Scarce: {categories['Scarce']}\n")

    print ("=== Dictionary Properties Demo ===")
    print ("Dictionary keys: ", end="")
    i = 0
    for key in inventory_dict.keys():
        print (key, end="")
        if (i != len(inventory_dict) - 1):
            print (", ", end="")
        i += 1
    print ("\nDictionary values: ", end="")
    i = 0
    for value in inventory_dict.values():
        print (value, end="")
        if (i != len(inventory_dict) - 1):
            print (", ", end="")
        i += 1
    exists_inv = 'sword' in inventory_dict
    print ("\nSample lookup - 'sword' in inventory:", exists_inv)
if (__name__ == "__main__"):
    main()