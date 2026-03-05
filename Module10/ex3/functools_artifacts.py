from typing import Any, Callable, Optional
from functools import reduce, singledispatch, partial, lru_cache
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> Optional[int]:
    if operation == "add":
        return reduce(add, spells, 0)
    elif operation == "mul":
        return reduce(mul, spells, 1)
    elif operation == "max":
        return reduce(max, spells)
    elif operation == "min":
        return reduce(min, spells)
    return None


def partial_enchanter(
    base_enchantment: Callable[..., Any]
) -> dict[str, Callable[..., Any]]:
    return {
        'fire_enchant': partial(base_enchantment, element='Fire', power=50),
        'ice_enchant': partial(base_enchantment, element='Ice', power=50),
        'lightning_enchant': partial(
            base_enchantment, element='Lightning', power=50
        )
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[..., None]:
    @singledispatch
    def spell_caster(spell: Any) -> None:
        print(f"Unsupported Format {spell.__class__.__name__} - {spell}")

    @spell_caster.register(int)
    def _cast_int(spell: int) -> None:
        print(f"casting spell with {spell} damage")

    @spell_caster.register(str)
    def _cast_str(spell: str) -> None:
        print(f"casting spell with {spell} enchantment")

    @spell_caster.register(list)
    def _cast_list(spell: list[Any]) -> None:
        for s in spell:
            spell_caster(s)
    return spell_caster


def main() -> None:
    try:
        print("Testing spell reducer...")
        powers = [10, 20, 30, 40]
        print(f"Sum: {spell_reducer(powers, 'add')}")
        print(f"Product: {spell_reducer(powers, 'mul')}")
        print(f"Max: {spell_reducer(powers, 'max')}")

        print("\nTesting partial enchanter...")

        def base_enchantment(item: str, element: str, power: int) -> str:
            return (
                f"{element} enchantment ({power} power)"
                f" applied to {item}"
            )
        enchants = partial_enchanter(base_enchantment)
        print(enchants['fire_enchant'](item="Sword"))
        print(enchants['ice_enchant'](item="Armor"))
        print(enchants['lightning_enchant'](item="Axe"))

        print("\nTesting memoized fibonacci...")
        fib = 10
        print(f"Fib({fib}): {memoized_fibonacci(fib)}")
        fib = 15
        print(f"Fib({fib}): {memoized_fibonacci(fib)}")

        print("\nTesting spell dispatcher...")
        caster = spell_dispatcher()
        caster(42)
        caster("Frost")
        caster(["Fire", 99])
        caster(0.1)
    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")


if __name__ == "__main__":
    main()
