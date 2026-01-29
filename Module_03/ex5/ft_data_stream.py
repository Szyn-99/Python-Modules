def events():
    yield "killed monster"
    yield "found treasure"
    yield "scored"
    yield "leveled up"

def players():
    yield "Alice"
    yield "Bob"
    yield "Charlie"
    yield "Diana"

def levels(num):
    for level in range(1, num + 1):
        yield level

def ft_data_stream(num):
    try:
        print("Starting data stream processing...")
        players_i = players()
        events_i = events()
        levels_i = levels(num)

        total_events = 0
        treasure_events = 0
        levelup_events = 0
        high_level_events = 0
        event_counter = 0
        while event_counter < num:
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
                levels_i = levels(num)
                level = next(levels_i)
                
            event_counter += 1
            if event == "found treasure":
                treasure_events += 1
            elif event == "leveled up":
                levelup_events += 1
            elif level == 10:
                high_level_events += 1
            total_events += 1
            print(f"Event {total_events}: Player {player} (level {level}) {event}")
    except Exception as e:
        print(f"Finished with error: {e}")
        
if __name__ == "__main__":
    ft_data_stream(50)