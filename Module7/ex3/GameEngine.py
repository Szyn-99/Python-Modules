from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory


class GameEngine:
    def __init__(self):
        self.engine_stats = {
            "turns_simulated": 0,
            "strategy_used": None,
            "total_damage": 0,
            "cards_created": 0,
        }
        self.hand = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.card_factory = factory
        self.game_strategy = strategy

    def simulate_turn(self) -> dict:
        self.stat["strategy_used"] = self.game_strategy.get_strategy_name()
        cards = self.card_factory.create_themed_deck(10)
        cards_list = [card for card_type in cards for card in cards[card_type]]
        cards_name = {
            card.name: sum(1 for c in cards_list if c.name == card.name)
            for card in cards_list
        }
        self.hand.extend(cards_name)
        self.hand = [f"{name} ({count})" for name, count in cards_name.items()]
        battlefield = self.card_factory.create_themed_deck(10)
        battlefield_list = [
            card for card_type in battlefield
            for card in battlefield[card_type]
        ]
        tr = self.game_strategy.execute_turn(cards_list, battlefield_list)
        self.stat["turns_simulated"] += 1
        self.stat["cards_created"] += self.card_factory.cards_created
        self.stat["total_damage"] += tr.get("damage_dealt", 0)
        return tr

    def get_engine_status(self) -> dict:
        return self.stat
