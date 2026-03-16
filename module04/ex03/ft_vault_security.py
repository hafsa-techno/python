print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating secure vault access...")

# SECURE EXTRACTION
try:
    with open("classified_data.txt", 'r') as file:
        print("Vault connection established with failsafe protocols")
        content = file.read()
        print("SECURE EXTRACTION:")
        print(content)
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
    content = ""

# SECURE PRESERVATION
with open("classified_data.txt", 'w') as file:
    file.write("[CLASSIFIED] New security protocols archived")

try:
    with open("classified_data.txt", 'r') as file:
        new_content = file.read()
        print("\nSECURE PRESERVATION:")
        print(new_content)
        print("Vault automatically sealed upon completion\n")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")

print("All vault operations completed with maximum security.")