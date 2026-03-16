import sys
print ("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

archivist_id = input ("Input Stream active. Enter archivist ID: ")
status_report = input ("Input Stream active. Enter status report: ")

sys.stdout.write(f"\n[STANDARD] Archive status from {archivist_id}: {status_report}\n")
sys.stderr.write("[ALERT] System dignostic: Communicatio channels verified\n")
sys.stdout.write("[STANDARD] Data transmission complete\n\n")

print ("Three-channel communication test successful.")