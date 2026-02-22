from ex0 import Card
class CreatureCard(Card):
    mana = 100
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack <= 0 or health <= 0:
            raise ValueError("Attack/Health cannot be negative or zero !")
        self.attack = attack
        self.health = health
    def play(self, game_state: dict) -> dict:
        if super().is_playable(self.mana):
            print(f"Playing {game_state['card_played']} with {game_state['mana_used']} mana available:")
            print("Playable: True")
            print(f"Play result: {{'card_played': '{game_state['card_played']}', 'mana_used': {game_state['mana_used']}"
                  f"'effect': 'Creature summoned to battlefield'}}")

    def attack_target(self, target) -> dict:
        pass