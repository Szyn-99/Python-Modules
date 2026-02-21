def main():
    from alchemy.grimoire.spellbook import record_spell
    from alchemy.grimoire.validator import validate_ingredients
    try:
        print("=== Circular Curse Breaking ===\n")
        print("Testing ingredient validation:")
        print(f'validate_ingredients("fire air"): '
              f'{validate_ingredients("fire air")}')
        print(f'validate_ingredients("dragon scales"): '
              f'{validate_ingredients("dragon scales")}\n')
        print("Testing spell recording with validation:")
        print(f'record_spell("Fireball", "fire air"): '
              f'{record_spell("Fireball", "fire air")}')
        print(f'record_spell("Dark Magic", "shadow"): '
              f'{record_spell("Dark Magic", "shadow")}')
        print('\nTesting late import technique:')
        print(f'record_spell("Lightning", "air"): '
              f'{record_spell("Lightning", "air")}')
        print("\nCircular dependency curse avoided using late imports!")
        print("All spells processed safely!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
