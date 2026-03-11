import sys

print ("=== Command Quest ===")
print ("\nProgram name:", sys.argv[0])
if (len(sys.argv) == 1):
    print ("No arguments provided!")
else:
    print (f"Arguments received:", len(sys.argv) - 1)
    count = 0
    for item in sys.argv:
        if (count != 0):
            print (f"Argument {count}: {item}")
        count += 1
print ("Total arguments:", len(sys.argv))