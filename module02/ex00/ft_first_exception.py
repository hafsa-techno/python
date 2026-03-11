def check_temperature(temp_str):
    try:
        num = int(temp_str)
        if (num < 0):
            print (f"Error: {num}°C is too cold for plants (min 0°C)")
        elif (num > 40):
            print (f"Error: {num}°C is too hot for plants (max 40°C)")
        else:
            print (f"Temperature {temp_str}°C is perfect for plants!")
        return (num)
    except ValueError:
        print (f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input():
    print ("Testing temperature: 25")
    check_temperature("25")
    print ("\n")
    print ("Testing temperature: abc")
    check_temperature("abc")
    print ("\n")
    print ("Testing temperature: 100")
    check_temperature("100")
    print ("\n")
    print ("Testing temperature: -50")
    check_temperature("-50")

print ("=== Garden Temperature Checker ===\n")
test_temperature_input()