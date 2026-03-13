from typing import Generator 
import time
data = [
    {
        "id": 1,
        "name": "alice",
        "level": 5,
        "type": "killed monster"
    },
    {
        "id": 2,
        "name": "bob",
        "level": 12,
        "type": "found treasure"
    },
    {
        "id": 3,
        "name": "bob",
        "level": 8,
        "type": "Level-up"
    },
    {
        "id": 4,
        "name": "charlie",
        "level": 3,
        "type": "completed quest"
    },
    {
        "id": 5,
        "name": "diana",
        "level": 10,
        "type": "killed monster"
    },
    {
        "id": 6,
        "name": "alice",
        "level": 6,
        "type": "found treasure"
    },
    {
        "id": 7,
        "name": "eric",
        "level": 15,
        "type": "defeated boss"
    },
    {
        "id": 8,
        "name": "frank",
        "level": 7,
        "type": "Level-up"
    },
    {
        "id": 9,
        "name": "charlie",
        "level": 4,
        "type": "found treasure"
    },
    {
        "id": 10,
        "name": "diana",
        "level": 11,
        "type": "completed quest"
    }
]

def infinite_gen(n) -> Generator[dict, None, None]:
    count = 0
    while (count < n):
        for item in data:
            yield {"id": count, **item}
            count += 1

def main():
    print ("Processing 1000 game events...")
    total_event = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0
    start_time = time.time()
    for item in infinite_gen(1000):
        if (item["level"] >= 10):
            high_level += 1
        if (item["type"] == "found treasure"):
            treasure_events += 1
        if (item["type"] == "Level-up"):
            level_up_events += 1
        total_event += 1
        print (f"Event {item["id"]}: Player {item["name"]} (level {item["level"]}) {item["type"]}")
    end_time = time.time()
    print (f"Total events processed: {total_event}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")

    print ("\n")
    print ("Memory usage: Constant (streaming)")
    gap = end_time - start_time
    print (f"Processing time: {gap:.3f} seconds")

    print ("\n=== Generator Demonstration ===")

if __name__ == "__main__":
    main()