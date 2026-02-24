from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from enum import Enum
from typing import Optional


class VeryImportant(Enum):
    important_flag = "!"


def dummy_method(flag: Optional[VeryImportant]) -> None:
    print(f"Polymorphism in action: Same interface, "
          f"different card behaviors{flag.important_flag.value}")


def main() -> None:
    try:
        print("\n=== DataDeck Deck Builder ===\n")
        print("Building deck with different card types...")
        deck = Deck()
        game_state = {"mana": 100}
        creature_card = CreatureCard("Fire Dragon", 5, "Rare", 7, 5)
        spell_card = SpellCard("Lightning Bolt", 3, "Common", "+3 damage")
        artifact_card = ArtifactCard(
            "Mana Crystal", 2, "Uncommon", 3, "Permanent: +1 mana per turn"
        )
        deck.add_card(creature_card)
        deck.add_card(spell_card)
        deck.add_card(artifact_card)
        print(f"Deck stats: {deck.get_deck_stats()}")
        print("\nDrawing and playing cards:\n")
        deck.shuffle()
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.__class__.__name__})")
        print(f"Play result: {card.play(game_state)}\n")
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.__class__.__name__})")
        print(f"Play result: {card.play(game_state)}\n")
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.__class__.__name__})")
        print(f"Play result: {card.play(game_state)}\n")

        dummy_method(VeryImportant.important_flag)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
