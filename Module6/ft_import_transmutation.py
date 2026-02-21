def main() -> None:
    try:
        print("=== Import Transmutation Mastery ===\n")
        print("Method 1 - Full module import:")
        import alchemy.elements
        print(f"alchemy.elements.create_fire(): "
              f"{alchemy.elements.create_fire()}\n")
        print("Method 2 - Specific function import:")
        from alchemy.elements import create_water
        print(f"create_water(): {create_water()}\n")
        print("Method 3 - Aliased import:")
        from alchemy.potions import healing_potion as heal
        print(f"heal(): {heal()}\n")
        print("Method 4 - Multiple imports:")
        from alchemy.elements import create_earth, create_fire
        from alchemy.potions import strength_potion
        print(f"create_earth(): {create_earth()}")
        print(f"create_fire(): {create_fire()}")
        print(f"strength_potion(): {strength_potion()}\n")
        print("All import transmutation methods mastered!")
    except Exception as e:
        print(f"Unhandled Error: {e}")


if __name__ == "__main__":
    main()
