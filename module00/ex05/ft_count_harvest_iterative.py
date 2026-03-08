def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for day in range(1, days + 1):
        print ("Day", day)
    print ("Harvest time!")
    
def main():
    ft_count_harvest_iterative()

if __name__ == "__main__":
    main()