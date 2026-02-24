from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = "Artifact"

    def play(self, game_state: dict) -> dict:
        if super().is_playable(game_state["mana"]):
            new_game_state = {}
            new_game_state["card_played"] = self.name
            new_game_state["mana_used"] = self.cost
            new_game_state["effect"] = self.effect
            game_state["mana"] -= self.cost
            return new_game_state

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            raise ValueError("Artifact is broken.")
        self.durability -= 1
        ability_result = {
            "card": self.name,
            "effect": self.effect,
            "durability remaining": self.durability,
        }
        return ability_result
