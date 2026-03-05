from typing import Any, Callable


def mage_counter() -> Callable[[], int]:
    counter = 0

    def closure() -> int:
        nonlocal counter
        counter += 1
        return counter
    return closure


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total_power = initial_power

    def accumulate_power(given_power: int) -> int:
        nonlocal total_power
        total_power += given_power
        return total_power
    return accumulate_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def apply_enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return apply_enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    storage: dict[Any, Any] = {}

    def store(key: Any, value: Any) -> None:
        storage.update({key: value})

    def recall(key: Any) -> Any:
        try:
            return storage[key]
        except KeyError:
            return "Memory not found"
    return {'store': store, 'recall': recall}


def main() -> None:
    try:
        print("Testing mage counter...")
        counter = mage_counter()
        print(f"Call 1: {counter()}")
        print(f"Call 2: {counter()}")
        print(f"Call 3: {counter()}")

        print("\nTesting spell accumulator...")
        accumulate = spell_accumulator(10)
        print(f"After 1st cast: {accumulate(20)}")
        print(f"After 2nd cast: {accumulate(30)}")
        print(f"After 3rd cast: {accumulate(-47)}")

        print("\nTesting enchantment factory...")
        flame_enchant = enchantment_factory("Flaming")
        frost_enchant = enchantment_factory("Frozen")
        print(flame_enchant("Sword"))
        print(frost_enchant("Shield"))

        print("\nTesting memory vault...")
        vault = memory_vault()
        vault['store']("secret_spell", "Dark Storm")
        vault['store']("password", "Manus123")
        print(f"Recall secret_spell: {vault['recall']('secret_spell')}")
        print(f"Recall password: {vault['recall']('password')}")
        print(f"Recall unknown: {vault['recall']('alo')}")
    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")


if __name__ == "__main__":
    main()
