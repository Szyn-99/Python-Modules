def ft_achievement_tracker() -> None:
    try:
        print("=== Achievement Tracker System ===\n")
        alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
        bob = {"first_kill", "level_10", "boss_slayer", "collector"}
        charlie = {
            "level_10",
            "treasure_hunter",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
        }

        all_achievements = alice.union(bob, charlie)
        common_achievements = alice.intersection(bob, charlie)
        rare_achievements = (
            set(alice.difference(bob, charlie))
            .union(bob.difference(alice, charlie))
            .union(charlie.difference(alice, bob))
        )
        alice_and_bob = alice.intersection(bob)
        alice_unique_bob = alice.difference(bob)
        bob_unique_alice = bob.difference(alice)
        print(f"Player alice achievements: {alice}")
        print(f"Player bob achievements: {bob}")
        print(f"Player charlie achievements: {charlie}\n")
        print("=== Achievement Analytics ===\n")
        print(f"All unique achievements: {all_achievements}")
        print(f"Total unique achievements: {len(all_achievements)}\n")
        print(f"Common to all players: {common_achievements}")
        print(f"Rare achievements (1 player): {rare_achievements}\n")
        print(f"Alice vs Bob common: {alice_and_bob}")
        print(f"Alice unique vs Bob: {alice_unique_bob}")
        print(f"Bob unique vs Alice: {bob_unique_alice}")

    except Exception as e:
        print(f"Error in achievement tracking: {e}")


if __name__ == "__main__":
    try:
        ft_achievement_tracker()
    except Exception as e:
        print(f"Unhandled error: {e}")
