def ft_plant_age():
    plant_age = int(input("Enter plant age in days: "))
    if (plant_age > 60):
        print ("Plant is ready to harvest!")
    else:
        print ("Plant needs more time to grow.")

def main():
    ft_plant_age()

if __name__ == "__main__":
    main()