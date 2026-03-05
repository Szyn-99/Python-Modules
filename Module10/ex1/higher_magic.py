from typing import Any, Callable


def spell_combiner(
    spell1: Callable[..., Any], spell2: Callable[..., Any]
) -> Callable[..., Any]:
    def combined_spell(*args: Any, **kwargs: Any) -> tuple[Any, Any]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined_spell


def power_amplifier(
    base_spell: Callable[..., Any], multiplier: int
) -> Callable[..., Any]:
    def spell_multiplier(*args: Any, **kwargs: Any) -> Any:
        return base_spell(*args, **kwargs) * multiplier
    return spell_multiplier


def conditional_caster(
    condition: Callable[..., Any], spell: Callable[..., Any]
) -> Callable[..., Any]:
    def only_if_true(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return only_if_true


def spell_sequence(spells: list[Callable[..., Any]]) -> Callable[..., Any]:
    def cast_all(*args: Any, **kwargs: Any) -> list[Any]:
        return [spell(*args, **kwargs) for spell in spells]
    return cast_all


def main() -> None:
    try:
        print("Testing spell combiner...")

        def fireball() -> str:
            return "Fireball hits Dragon"

        def heal() -> str:
            return "Heals Dragon"

        combined = spell_combiner(fireball, heal)
        result = combined()
        print(f"Combined spell result: {result[0]}, {result[1]}")

        print("\nTesting power amplifier...")

        def base_power() -> int:
            return 10

        amplified = power_amplifier(base_power, 3)
        print(f"Original: {base_power()}, Amplified: {amplified()}")

        print("\nTesting conditional caster...")

        def yes_mana() -> bool:
            return True

        def no_mana() -> bool:
            return False

        def lightning() -> str:
            return "Dark pursuers launched"

        cast_with_mana = conditional_caster(yes_mana, lightning)
        cast_without_mana = conditional_caster(no_mana, lightning)
        print(f"With mana: {cast_with_mana()}")
        print(f"Without mana: {cast_without_mana()}")

        print("\nTesting spell sequence...")

        def dark_orb() -> str:
            return "Dark orb casted"

        def shield() -> str:
            return "Shield raised"

        def heal_spell() -> str:
            return "Heal applied"

        def pine_resin() -> str:
            return "Dark pine resin applied"

        def dark_sword() -> str:
            return "Dark Sword summoned"

        spells = [dark_orb, shield, heal_spell, pine_resin, dark_sword]
        cast_sequence = spell_sequence(spells)
        for result in cast_sequence():
            print(f"{result}")
    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")


if __name__ == "__main__":
    main()
