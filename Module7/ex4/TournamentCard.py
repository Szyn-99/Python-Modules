from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name, cost, rarity, attack_power, defense, health):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.health = health
        self.record = {"wins": 0, "losses": 0}
        self.id = f"{self.name.lower().split()[1]}_001"

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

    def update_wins(self, wins: int) -> None:
        self.record["wins"] += wins

    def update_losses(self, losses: int) -> None:
        self.record["losses"] += losses

    def attack(self, target) -> dict:
        attack_result = {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_power,
            "combat_type": "melee",
        }
        target.health -= self.attack_power
        return attack_result

    def calculate_rating(self) -> int:
        return self.health + self.attack_power

    def get_tournament_stats(self) -> dict:
        multiple_inheritance_classes = [
            base.__name__ for base in self.__class__.__bases__
        ]
        return {
            "interface": multiple_inheritance_classes,
            "attack_power": self.attack_power,
            "defense": self.defense,
            "health": self.health,
            "rating": self.calculate_rating(),
            "record": f"({self.record['wins']}-{self.record['losses']})",
        }

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

    def get_rank_info(self) -> dict:
        return {
            "rating": self.calculate_rating(),
            "record": f"({self.record['wins']}-{self.record['losses']})",
        }
