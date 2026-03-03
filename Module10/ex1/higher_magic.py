from typing import Any, Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell() -> tuple:
        return (spell1(), spell2())
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def spell_multiplier() -> Any:
        return base_spell() * multiplier
    return spell_multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def only_if_true() -> str:
        if condition():
            return spell()
        else:
            return "Spell fizzled"
    return only_if_true


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_all() -> list:
        return [spell() for spell in spells]
    return cast_all


def main():
    try:
        print("Testing spell combiner...")

        def fireball():
            return "Fireball hits Dragon"

        def heal():
            return "Heals Dragon"

        combined = spell_combiner(fireball, heal)
        result = combined()
        print(f"Combined spell result: {result[0]}, {result[1]}")

        print("\nTesting power amplifier...")

        def base_power():
            return 10

        amplified = power_amplifier(base_power, 3)
        print(f"Original: {base_power()}, Amplified: {amplified()}")

        print("\nTesting conditional caster...")

        def has_mana():
            return True

        def no_mana():
            return False

        def lightning():
            return "Dark pursuers launched"

        cast_with_mana = conditional_caster(has_mana, lightning)
        cast_without_mana = conditional_caster(no_mana, lightning)
        print(f"With mana: {cast_with_mana()}")
        print(f"Without mana: {cast_without_mana()}")

        print("\nTesting spell sequence...")

        def dark_orb():
            return "Dark orb casted"

        def shield():
            return "Shield raised"

        def heal_spell():
            return "Heal applied"

        def pine_resin():
            return "Dark pine resin applied"

        def dark_sword():
            return "Dark Sword summoned"

        spells = [dark_orb, shield, heal_spell, pine_resin, dark_sword]
        cast_sequence = spell_sequence(spells)
        for result in cast_sequence():
            print(f"{result}")
    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")


if __name__ == "__main__":
    main()
