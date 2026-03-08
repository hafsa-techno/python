def ft_count_harvest_recursive_helper(n, days):

    if (days == n):
        print ("Day ", days)
        return
    days = days - 1
    ft_count_harvest_recursive_helper(n, days)
    print ("Day ", days + 1)
    

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_count_harvest_recursive_helper(1, days)
    print ("Harvest time!")
def main():
    ft_count_harvest_recursive()

if __name__ == "__main__":
    main()