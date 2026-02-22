from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.consumable = True
        self.type = "Spell"
    def play(self, game_state: dict) -> dict:
        new_game_state = {}
        try:
            if super().is_playable(game_state['mana']) and self.consumable:
                new_game_state['card_played'] = self.name
                new_game_state['mana_used'] = self.cost
                new_game_state['effect'] = self.effect_type
                game_state['mana'] -= self.cost
                self.consumable = False
                return new_game_state
            else:
                raise ValueError("Spell cannot be played, Spell already consumed.")
        except ValueError:
            raise
        finally:
            return new_game_state
    def resolve_effect(self, targets: list) -> dict:
        effect_result = {
            "card": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "effect_resolved": True
        }
        return effect_result