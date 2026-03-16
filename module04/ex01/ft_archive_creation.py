print ("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

print ("Initializing new storage unit: new_discovery.txt")
try:
    new_file = open("new_discovery.txt", 'w')
    print ("Storage unit created successfully...\n")
    print ("Inscribing preservation data...")
    new_file.write("[ENTRY 001] New quantum algorithm discovered\n")
    new_file.write("[ENTRY 002] Efficiency increased by 347%\n")
    new_file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    new_file.close()
except IOError as e:
    print (f"An error occured: {e}")

try:
    file = open("new_discovery.txt", 'r')
    text = file.read()
    print (text)
    file.close()
    print ("Data inscription complete. Storage unit sealed")
    print ("Archive 'new_discovery.txt' ready for long-term preservation.")
except FileNotFoundError:
    print ("ERROR: file not found.")

