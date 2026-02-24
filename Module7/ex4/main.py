from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main():
    # try:
    print("\n=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")
    tournament = TournamentPlatform()
    first_card = TournamentCard("Fire Dragon", 5, "legendary", 1000, 5, 200)
    second_card = TournamentCard("Ice Wizard", 3, "common", 1000, 3, 150)
    card_1 = tournament.register_card(first_card)
    card_2 = tournament.register_card(second_card)
    print(card_1)
    print(card_2)

    print("Creating tournament match...")
    match_result = tournament.create_match(first_card.id, second_card.id)
    print(f"Match result: {match_result}\n")
    print("Tournament Leaderboard:\n")
    tournament.get_leaderboard()
    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())

    print(
        "\nTournament Platform: Multiple Inheritance + Combat +"
        " Ranking System implemented successfully!"
    )
    # except Exception as e:
    #     print(f"Error: {e}")


main()
