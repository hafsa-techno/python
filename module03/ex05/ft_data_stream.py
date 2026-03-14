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

def game_events():
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

def fibonacci(n):
    i = 2
    prev_prev = 0
    prev = 1
    current = 0
    while i <= n:
        current = prev + prev_prev
        prev_prev = prev
        prev = current
        i += 1
    return (current)

def fibonacci_infinite_gen(n) ->Generator[int, None, None]:
    i = 0
    while i < n:
        yield fibonacci(i)
        i += 1

def is_prime(n):
    if (n < 2):
        return False
    i = 2
    while (i < n):
        if (n % i == 0):
            return False
        i += 1
    return True

def prime_generate_infinte(n) -> Generator[int, None, None]:
    i = 0
    while (i < n):
        if (is_prime(i)):
            yield i
        i += 1

def main():
    game_events()

    print ("\n=== Generator Demonstration ===")
    n = 10
    print (f"Fibonacci sequence (first {n}): ", end="")
    count = 0
    for item in fibonacci_infinite_gen(n):
        print (item, end="")
        if (count != n - 1):
            print (", ", end="")
        count += 1
    print ("\n")
    n = 5
    print (f"Prime numbers (first {n}) ", end="")
    for item in prime_generate_infinte(n):
        print (item, end=" ")
    print ("\n")
if __name__ == "__main__":
    main()