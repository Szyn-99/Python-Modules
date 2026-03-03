from typing import Any, Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def decorator_job(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        chrono_start = time.time()
        aftermath = func(*args, **kwargs)
        print(f"Spell completed in {time.time() - chrono_start:.2f} seconds")
        return aftermath
    return decorator_job


def power_validator(min_power: int) -> Callable:
    def decorator_job(function: Callable) -> Callable:
        @wraps(function)
        def decorator(*args, **kwargs) -> Any:
            power = kwargs.get('power', args[-1] if args else 0)
            if power >= min_power:
                return function(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return decorator
    return decorator_job


def retry_spell(max_attempts: int) -> Callable:
    def decorator_job(function: Callable) -> Callable:
        @wraps(function)
        def decorator(*args, **kwargs) -> Any:
            for attempt in range(max_attempts):
                try:
                    return function(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt})")
            print(f"Spell casting failed after {max_attempts} attempts")
        return decorator
    return decorator_job


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not name or len(name.strip()) < 3:
            return False
        if not name.isalpha():
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():
    try:
        print("Testing spell timer...")

        @spell_timer
        def fireball():
            chrono = 1.337
            time.sleep(chrono)
            return "Fireball cast!"
        result = fireball()
        print(f"Result: {result}")

        print("\nTesting power validator (standalone)...")

        @power_validator(20)
        def dark_magic(spell: str, power: int) -> str:
            return f"{spell} unleashed with {power} power!"
        print(dark_magic("Shadow Bolt", 50))
        print(dark_magic("Spark", 5))

        print("\nTesting MageGuild...")
        guild = MageGuild()
        print(MageGuild.validate_mage_name("DarkWraith"))
        print(MageGuild.validate_mage_name("hh"))
        print(guild.cast_spell("DarkMoon", 15))
        print(guild.cast_spell("pyromancy small fireball", 5))

        print("\nTesting retry spell (succeeds on attempt 3)...")
        call_count = 0

        @retry_spell(max_attempts=5)
        def unstable_spell() -> str:
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise RuntimeError("Spell missed the enemy!")
            return "Spell casted succesfully!"
        print(f"Result: {unstable_spell()}")

        print("\nTesting retry spell (always fails)...")

        @retry_spell(max_attempts=3)
        def doomed_spell() -> str:
            raise RuntimeError("Critical failure!")
        result = doomed_spell()
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")


if __name__ == "__main__":
    main()
