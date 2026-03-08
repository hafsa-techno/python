def ft_garden_summary():
    name = input ("Enter garden name: ")
    nbr_plants = int(input("Enter number of plants: "))
    print ("Garden: ", name)
    print ("Plants: ", nbr_plants)
    print ("Status: Growing well!")

def main():
    ft_garden_summary()

if __name__ == "__main__":
    main()