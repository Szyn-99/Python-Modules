from ex3.GameStrategy import GameStrategy
import random


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        actions = {
            "cards_played": [],
            "mana_used": 0,
            "targets_attacked": [],
            "damage_dealt": 0,
        }
        mana = 10
        for card in hand:
            game_stats = {"mana": mana}
            if card.type == "Creature" and mana >= card.cost:
                game_stats = card.play(game_stats)
                actions["cards_played"].append(card.name)
                actions["mana_used"] += card.cost
                mana -= card.cost
                target = random.choice(battlefield)
                attack_result = card.attack_target(target)
                if not attack_result["combat_resolved"]:
                    continue
                actions["targets_attacked"].append(target.name)
                actions["damage_dealt"] += attack_result["damage_dealt"]
            elif card.type == "Spell" and mana >= card.cost:
                game_stats = card.play(game_stats)
                actions["cards_played"].append(card.name)
                actions["mana_used"] += card.cost
            elif card.type == "Artifact" and mana >= card.cost:
                game_stats = card.play(game_stats)
                actions["cards_played"].append(card.name)
                actions["mana_used"] += card.cost
        if not actions["targets_attacked"]:
            actions["targets_attacked"] = None
        return actions

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        possible_targets = []
        i = 0
        while i < len(available_targets) / 2:
            target = random.choice(available_targets)
            if target not in possible_targets and target.health > 0:
                possible_targets.append(target)
            i += 1
        return possible_targets
