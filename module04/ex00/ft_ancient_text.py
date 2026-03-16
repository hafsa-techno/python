print ("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
print ("Accessing Storage Vault: ancient_fragment.txt")


try:
    file = open("ancient_fragment.txt", 'r')
    print ("Connection established...\n")
    text = file.read()
    print ("RECOVERED DATA:")
    print (text, "\n")
    file.close()
    print ("Data recovery complete. Storage unit disconnected.")
except FileNotFoundError:
    print ("ERROR: Storage vault not found. Run data generator first.")
