import alchemy

def main() -> None:
    print("=== Pathway Debate Mastery ===\n")
    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {alchemy.transmission.lead_to_gold()}")
    print(f"stone_to_gem(): {alchemy.stone_to_gem()}")
    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {alchemy.philosophers_stone()}")
    print(f"elixir_of_life(): {alchemy.elixir_of_life()}")
    print("\nTesting Package Access:")
    print(f"alchemy.transmutation.lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")

if __name__ == "__main__":
    main()