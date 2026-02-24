from ex0.CreatureCard import CreatureCard


def main() -> None:
    try:
        print("\n=== DataDeck Card Foundation ===\n")
        print("Testing Abstract Base Class Design:\n")
        game_state = {"mana": 6}
        fire_dragon = CreatureCard("Fire Dragon", 5, "Epic", 7, 15)
        print("CreatureCard Info:")
        fire_dragon.get_card_info()
        print(f"\nPlaying Fire Dragon with"
              f" {game_state['mana']} mana available:")
        print(f"Playable: {fire_dragon.is_playable(game_state['mana'])}")
        print(f"Play result: {fire_dragon.play(game_state)}\n")
        goblin_warrior = CreatureCard("Goblin Warrior", 2, "Common", 3, 5)
        print(f"{fire_dragon.name} attacks {goblin_warrior.name}:")
        attack_result = fire_dragon.attack_target(goblin_warrior)
        print(
            f"Atack Result: {{'attacker': '{attack_result['attacker']}', "
            f"'target': '{attack_result['target']}', "
            f"'damage_dealt': {attack_result['damage_dealt']}, "
            f"'combat_resolved': {attack_result['combat_resolved']}}}"
        )

        print()
        print(f"Testing insufficient mana ({game_state['mana']} available):")
        print(f"Playable: {fire_dragon.is_playable(game_state['mana'])}")
        print("\nAbstract pattern successfully demonstrated!")
    except Exception as e:
        print(f"Error: {e}")


main()
