def garden_operations():
    print ("=== Garden Error Types Demo ===")
    print ("Testing ValueError...")
    try:
        num = int("abc")
    except ValueError:
        print ("Caught ValueError: invalid literal for int()\n")
    print ("Testing ZeroDivisionError...")
    try:
        num = 9 / 0
    except ZeroDivisionError:
        print ("Caught ZeroDivisionError: division by zero\n")
    print ("Testing FileNotFoundError...")
    try:
        file = open ("missing.txt")
        file.close()
    except FileNotFoundError:
        print ("Caught FileNotFoundError: No such file 'missing.txt'\n")
    print ("Testing KeyError...")
    try:
        plants = {"rose":"red", "sunflower": "yellow"}
        print (plants["missing_plant"])
    except KeyError:
        print ("Caught KeyError: 'missing_plant'\n")


def test_error_types():
    garden_operations()
    print ("Testing multiple errors together...")
    try:
        num = int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print ("Caught an error, but program continues!\n")

    print ("All error types tested successfully!")

test_error_types()