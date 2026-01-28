def getting_data(num_events=100):
    players = ("Alice", "Bob", "Charlie", "Diana")
    events = ("killed monster", "found treasure", "scored", "leveled up")
    levels = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    

def ft_data_stream():
    try:
        print("Starting data stream processing...")
        players, events, levels = getting_data()
        total_events = 0
        treasure_events = 0
        levelup_events = 0
        high_level_events = 0
        for player in players:
            for event in events:
                if event == "found treasure":
                    treasure_events += 1
                elif event == "leveled up":
                    levelup_events += 1
                elif levels == 10:
                    high_level_events += 1
                total_events += 1
                print(f"Event {total_events}: Player {player} (level 5) {event}")
    except Exception as e:
        print(f"Finished with error: {e}")
        
if __name__ == "__main__":
    ft_data_stream()