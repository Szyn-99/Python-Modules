from ex0.Card import Card
class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack <= 0 or health <= 0:
            raise ValueError("Attack/Health cannot be negative or zero.")
        self.attack = attack
        self.health = health
        self.type = "Creature"
    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info.update({
            "attack": self.attack,
            "health": self.health,
            "type": self.type
        })
        print(card_info)
        return card_info
    def play(self, game_state: dict) -> dict:
        if super().is_playable(game_state['mana']):
            new_game_state = {}
            new_game_state['card_played'] = self.name
            new_game_state['mana_used'] = self.cost
            new_game_state['effect'] = "Creature summoned to battlefield"
            game_state['mana'] -= self.cost
            return new_game_state
        return game_state

    def attack_target(self, target) -> dict:
        if not isinstance(target, CreatureCard):
            return {'combat_resolved': False}
        if self.health <= 0:
            raise ValueError("This creature is already dead.")
        if target.health <= 0:
            raise ValueError("Target creature is already dead.")
        target.health -= self.attack
        attack_result = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
        return attack_result