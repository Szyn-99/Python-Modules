from ex2.EliteCard import EliteCard
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


def main():
    try:
        print("\n=== DataDeck Ability System ===\n")
        print("EliteCard capabilities:")

        cards_attributes = [
            att
            for att in dir(Card)
            if not att.startswith("__") and not att.startswith("_")
        ]
        combatable_cards_attributes = [
            att
            for att in dir(Combatable)
            if not att.startswith("__") and not att.startswith("_")
        ]
        magical_cards_attributes = [
            att
            for att in dir(Magical)
            if not att.startswith("__") and not att.startswith("_")
        ]

        print(f"- Card: {cards_attributes}\n")
        print(f"- Combatable: {combatable_cards_attributes}\n")
        print(f"- Magical: {magical_cards_attributes}\n")

        elite_card = EliteCard(
            name="Arcane Warrior",
            cost=4,
            rarity="Epic",
            attack_power=5,
            defense=5,
            magic_power=6,
        )
        card = EliteCard(
            name="Enemy",
            cost=2,
            rarity="Common",
            attack_power=3,
            defense=2,
            magic_power=1,
        )

        print(f"Playing {elite_card.name} (Elite Card):")

        print("\nCombat phase:")

        attack_result = elite_card.attack(card)
        print(f"Attack Result: {attack_result}")
        defend_result = elite_card.defend(card.attack_power)
        print(f"Defense Result: {defend_result}")

        print("\nMagic phase:")
        spell_cast = elite_card.cast_spell("Fireball", [card])
        print(f"Spell cast: {spell_cast}")
        mana_channel = elite_card.channel_mana(3)
        print(f"Mana channel: {mana_channel}")

        print("\nMultiple interface implementation successful!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
