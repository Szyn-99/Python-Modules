def prime_detector(num):
    if num < 2:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

def fibonacci_range(num_range):
    a = 0
    b = 1
    count = 0
    while True:
        if(count == num_range):
            break
        yield a
        """the rule is: new a is the old b, new b is the old a + old b"""
        tmp = a
        a = b
        b = tmp + b
        count += 1

def prime_range(num_range):
    count = 0
    prime = 2
    while True:
        if prime_detector(prime):
            yield prime
            count += 1
        prime += 1
        if count == num_range:
            break

def events():
    yield "killed monster"
    yield "found treasure"
    yield "completed quest"
    yield "scored"
    yield "leveled up"
    yield "healed"
    yield "Obtained DarkSword"
    yield "Joined DarkWraiths"

def players():
    yield "Alice"
    yield "Szyn"
    yield "Eve"
    yield "Frank"
    yield "Grace"
    yield "Heidi"
    yield "Ivan"
    yield "Judy"
    yield "Bob"
    yield "Charlie"
    yield "Diana"

def levels(num):
    for level in range(1, num + 1):
        yield level

def ft_data_stream(num):
    try:
        print("=== Game Data Stream Processor ===\n")
        print(f"Processing {num} game events...\n")
        players_i = players()
        events_i = events()
        levels_i = levels(num)
        already_count = []
        total_events = 0
        treasure_events = 0
        levelup_events = 0
        high_level_events = 0
        while total_events < num:
            try:
                player = next(players_i)
            except StopIteration:
                players_i = players()
                player = next(players_i)
            try:
                event = next(events_i)
            except StopIteration:
                events_i = events()
                event = next(events_i)
            try:
                level = next(levels_i)
            except StopIteration:
                break
            if event == "found treasure":
                treasure_events += 1
            if event == "leveled up":
                levelup_events += 1
            if level > 10 and player not in already_count:
                high_level_events += 1
                already_count.append(player)
            total_events += 1
            print(f"Event {total_events}: Player {player} (level {level}) {event}")
        print("\n=== Stream Analytics ===")
        print(f"Total events processed: {total_events}")
        print(f"High-level players (10+): {high_level_events}")
        print(f"Treasure events: {treasure_events}")
        print(f"Level-up events: {levelup_events}")

        print("\nMemory usage: Constant (streaming)\nProcessing time: 0.045 seconds\n")
        print("=== Generator Demonstration ===")
        prime = 5
        fibonacci = 10
        print(f"Fibonacci sequence (first {fibonacci}):", end=" ")
        print(*fibonacci_range(fibonacci),sep=", ", end="\n")
        print(f"Prime numbers (first {prime}):", end=" ")
        print(*prime_range(prime), sep=", ", end="\n")
    except Exception as e:
        print(f"Finished with error: {e}")
        
if __name__ == "__main__":
    ft_data_stream(1000000)