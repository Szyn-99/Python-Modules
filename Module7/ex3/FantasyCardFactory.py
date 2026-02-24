from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory
import random


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.cards_created = 0
        self.cards_types = {"creature": 0, "spell": 0, "artifact": 0}
        self.available_types = {"creature": [], "spell": [], "artifact": []}
        self.random_cost_list = [1, 2, 3, 4, 5]
        self.random_attack_power_list = [1, 2, 3, 4]
        self.random_health_list = [5, 6, 7, 8, 9, 10]
        self.random_durability_list = [3, 4, 5, 6, 7, 8, 9, 10]
        self.random_rarity_list = ["Common", "Uncommon", "Rare",
                                   "Epic", "Legendary", "Divine"]
        self.random_effect_types = ["Damage", "Heal", "Buff",
                                    "Debuff", "Utility"]
        self.random_effect_list = ["Draw Card", "Discard Card", "Gain Mana"]
        self.random_creature_names = ["Goblin", "Elf",
                                      "Dragon", "Knight"]
        self.random_spell_names = ["Fireball", "Lightning Bolt", "Frost Nova"]
        self.random_artifact_names = ["Sword of Power", "Shield of Resilience",
                                      "Amulet of Wisdom"]

    def create_creature(self, name_or_power=None):
        if isinstance(name_or_power, str):
            self.cards_created += 1
            self.cards_types["creature"] += 1
            self.available_types["creature"].append(name_or_power)
            return CreatureCard(
                name_or_power,
                random.choice(self.random_cost_list),
                random.choice(self.random_rarity_list),
                random.choice(self.random_attack_power_list),
                random.choice(self.random_health_list),
            )
        elif isinstance(name_or_power, int):
            self.cards_created += 1
            self.cards_types["creature"] += 1
            self.available_types["creature"].append(f"Number {name_or_power}")
            return CreatureCard(
                f"Number {name_or_power}",
                random.choice(self.random_cost_list),
                random.choice(self.random_rarity_list),
                random.choice(self.random_attack_power_list),
                random.choice(self.random_health_list),
            )
        else:
            self.cards_created += 1
            self.cards_types["creature"] += 1
            self.available_types["creature"].append("Nameless Creature")
            return CreatureCard(
                "Nameless Creature",
                random.choice(self.random_cost_list),
                random.choice(self.random_rarity_list),
                random.choice(self.random_attack_power_list),
                random.choice(self.random_health_list),
            )

    def create_spell(self, name_or_power=None):
        if isinstance(name_or_power, str):
            self.cards_created += 1
            self.cards_types["spell"] += 1
            self.available_types["spell"].append(name_or_power)
            return SpellCard(
                name_or_power,
                random.choice(self.random_cost_list),
                random.choice(self.random_rarity_list),
                random.choice(self.random_effect_types),
            )
        elif isinstance(name_or_power, int):
            self.cards_created += 1
            self.cards_types["spell"] += 1
            self.available_types["spell"].append(f"Number {name_or_power}")
            return SpellCard(
                f"Number {name_or_power}",
                random.choice(self.random_cost_list),
                random.choice(self.random_rarity_list),
                random.choice(self.random_effect_types),
            )
        else:
            self.cards_created += 1
            self.cards_types["spell"] += 1
            self.available_types["spell"].append("Nameless Spell")
            return SpellCard(
                "Nameless Spell",
                random.choice(self.random_cost_list),
                random.choice(self.random_rarity_list),
                random.choice(self.random_effect_types),
            )

    def create_artifact(self, name_or_power=None):
        if isinstance(name_or_power, str):
            self.cards_created += 1
            self.cards_types["artifact"] += 1
            self.available_types["artifact"].append(name_or_power)
            return ArtifactCard(
                name_or_power,
                random.choice(self.random_cost_list),
                random.choice(self.random_rarity_list),
                random.choice(self.random_durability_list),
                random.choice(self.random_effect_list),
            )
        elif isinstance(name_or_power, int):
            self.cards_created += 1
            self.cards_types["artifact"] += 1
            self.available_types["artifact"].append(f"Number {name_or_power}")
            return ArtifactCard(
                f"Number {name_or_power}",
                random.choice(self.random_cost_list),
                random.choice(self.random_rarity_list),
                random.choice(self.random_durability_list),
                random.choice(self.random_effect_list),
            )
        else:
            self.cards_created += 1
            self.cards_types["artifact"] += 1
            self.available_types["artifact"].append("Nameless Artifact")
            return ArtifactCard(
                "Nameless Artifact",
                random.choice(self.random_cost_list),
                random.choice(self.random_rarity_list),
                random.choice(self.random_durability_list),
                random.choice(self.random_effect_list),
            )

    def create_themed_deck(self, size: int):
        deck = {"creature": [], "spell": [], "artifact": []}
        for card in range(size):
            card_type = random.choice(["creature", "spell", "artifact"])
            if card_type == "creature":
                self.cards_created += 1
                self.cards_types["creature"] += 1
                deck["creature"].append(
                    self.create_creature(
                        random.choice(self.random_creature_names)
                        )
                )
            elif card_type == "spell":
                self.cards_created += 1
                self.cards_types["spell"] += 1
                deck["spell"].append(
                    self.create_spell(
                        random.choice(self.random_spell_names)
                        )
                )
            else:
                self.cards_created += 1
                self.cards_types["artifact"] += 1
                deck["artifact"].append(
                    self.create_artifact(
                        random.choice(self.random_artifact_names)
                        )
                )
        return deck

    def get_supported_types(self):
        return {"supported_types": ["creature", "spell", "artifact"]}
