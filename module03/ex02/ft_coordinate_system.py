import math

def main():

    print ("=== Game Coordinate System ===\n")

    tuple1 = tuple((10, 20, 5))
    print ("Position created:", tuple1)
    x1, y1, z1 = tuple1
    distance = math.sqrt(x1 * x1 + y1 * y1 + z1 * z1)
    print (f"Distance Between (0, 0, 0) and (10, 20, 5): {distance:.2f}\n")


    str = "3,4,0"
    print (f'Parsing coordinates: "{str}"')
    lst = str.split(",")
    for i in range (len(lst)):
        lst[i] = int(lst[i])
    tuple2 = tuple(lst)
    print ("Parsed position:",tuple2)
    x2, y2, z2 = tuple2
    distance = math.sqrt(x2 * x2 + y2 * y2 + z2 * z2)
    print (f"Distance between (0, 0, 0) and ({tuple2}): {distance}\n")


    try:
        str = "abc,def,ghi"
        print (f'Parsing invalid coordinates: "{str}"')
        lst = str.split(",")
        for i in range (len(lst)):
            lst[i] = int(lst[i])
    except ValueError as e:
        print (f"Error parsing coordinates: {e}")
        print (f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")

    print ("Unpacking demonstration:")
    print (f"Player at x={x2}, y={y2}, z={z2}")
    print (f"Coordinates: X={x2}, Y={z2}, Z={z2}")

if __name__ == "__main__":
    main()
