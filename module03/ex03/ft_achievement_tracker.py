print ("=== Achievement Tracker System ===")

alice_ach = {'first_kill', 'level_10','treasure_hunter','speed_demon'}
bob_ach = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie_ach = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}

print ("Player alice achievements:", alice_ach)
print ("Player bob achievements:", bob_ach)
print ("Player charlie achievements:", charlie_ach)

print ("\n === Achievement Analytics ===")
unique_ach = alice_ach.union(bob_ach, charlie_ach)
print ("All unique achievements:", unique_ach)
print ("Total unique achievements:", len(unique_ach))

print ("\nCommon to all players:",alice_ach.intersection(bob_ach, charlie_ach))

df_al = alice_ach.difference(bob_ach, charlie_ach)
df_bob = bob_ach.difference(alice_ach, charlie_ach)
df_char = charlie_ach.difference(alice_ach, bob_ach)
print ("Rare achievements (1 player):", df_al.union(df_bob, df_char))

print ("\n")
print ("Alice vs Bob common: ",alice_ach.intersection(bob_ach))
print ("Alice unique: ",alice_ach.difference(bob_ach))
print ("Bob unique: ",bob_ach.difference(alice_ach))