from .spellbook import record_spell
from .validator import validate_ingredients

if __name__ == "__main__":
    record_spell("Test Spell", "fire")
    print(validate_ingredients("fire"))
