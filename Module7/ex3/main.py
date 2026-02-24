from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    try:
        print("\n=== DataDeck Game Engine ===\n")
        print("Configuring Fantasy Card Game...")
        card_game = GameEngine()
        fantasy_cards = FantasyCardFactory()
        aggressive_strategy = AggressiveStrategy()
        card_game.configure_engine(fantasy_cards, aggressive_strategy)
        print(f"Factory: {fantasy_cards.__class__.__name__}")
        print(f"Strategy: {aggressive_strategy.get_strategy_name()}")
        _ = [
            fantasy_cards.create_creature("dragon"),
            fantasy_cards.create_creature("goblin"),
            fantasy_cards.create_spell("fireball"),
            fantasy_cards.create_artifact("mana_ring"),
        ]
        print(f"Available types: {fantasy_cards.available_types}\n")

        print("Simulating aggressive turn...")
        turn_result = card_game.simulate_turn()
        print(f"Hand: {card_game.hand}\n")
        print("Turn execution:")
        print(f"Strategy: {aggressive_strategy.get_strategy_name()}")
        print(f"Actions: {turn_result}\n")
        print("Game Report:")
        print(card_game.get_engine_status())
        print("\nAbstract Factory + Strategy Pattern:"
              "Maximum flexibility achieved!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
