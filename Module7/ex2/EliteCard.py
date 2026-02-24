from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense: int,
        magic_power: int,
    ):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.magic_power = magic_power
        self.type = "Elite"
        self.health = 100
        self.mana = 8

    def play(self, game_state: dict) -> dict:
        if super().is_playable(game_state["mana"]):
            new_game_state = {}
            new_game_state["card_played"] = self.name
            new_game_state["mana_used"] = self.cost
            new_game_state["attack_power"] = self.attack_power
            new_game_state["defense"] = self.defense
            new_game_state["magic_power"] = self.magic_power
            game_state["mana"] -= self.cost
            return new_game_state

    def attack(self, target) -> dict:
        attack_result = {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_power,
            "combat_type": "melee",
        }
        target.health -= max(0, self.attack_power - target.defense)
        return attack_result

    def defend(self, incoming_damage: int) -> dict:
        self.health -= max(0, incoming_damage - self.defense)
        defend_result = {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": (
                self.defense - incoming_damage
                if self.defense > incoming_damage else 0
            ),
            "still_alive": self.health > 0,
        }

        return defend_result

    def get_combat_stats(self) -> dict:
        return {
            "attack_power": self.attack_power,
            "defense": self.defense,
            "health": self.health,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        spell_result = {
            "caster": self.name,
            "spell": spell_name,
            "targets": [target.name for target in targets],
            "mana used": self.cost,
        }
        self.mana -= self.cost
        return spell_result

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        mana_result = {"channeled": amount, "total_mana": self.mana}
        return mana_result

    def get_magic_stats(self) -> dict:
        return {"magic_power": self.magic_power, "mana": self.mana}
