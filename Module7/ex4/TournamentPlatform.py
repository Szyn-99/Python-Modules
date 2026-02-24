from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.registered_cards = {}
        self.leaderboard = []
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise ValueError("Only TournamentCard can be registered.")
        self.registered_cards[card.id] = card
        info = card.get_tournament_stats()
        return (
            f"{card.name.capitalize()} (ID: {card.id}):\n"
            f"- Interfaces: {info['interface']}\n"
            f"- Rating: {info['rating']}\n"
            f"- Record: {info['record']}\n"
        )

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card_1 = self.registered_cards.get(card1_id)
        card_2 = self.registered_cards.get(card2_id)
        if not card_1 or not card_2:
            raise ValueError("One or both cards are not registered.")
        if card_1.health <= 0 or card_2.health <= 0:
            raise ValueError("One or both cards are dead.")
        self.matches_played += 1
        while card_1.health > 0 and card_2.health > 0:
            card_1.attack(card_2)
            if card_2.health <= 0:
                card_1.update_wins(1)
                card_2.update_losses(1)
                self.leaderboard.extend([card_1, card_2])
                return {
                    "winner": card_1.name,
                    "loser": card_2.name,
                    "winner_rating": card_1.calculate_rating() + 16,
                    "loser_rating": card_2.calculate_rating() - 16,
                }
            card_2.attack(card_1)
            if card_1.health <= 0:
                card_2.update_wins(1)
                card_1.update_losses(1)
                self.leaderboard.extend([card_2, card_1])
                return {
                    "winner": card_2.name,
                    "loser": card_1.name,
                    "winner_rating": card_2.calculate_rating() + 16,
                    "loser_rating": card_1.calculate_rating() - 16,
                }

    def get_leaderboard(self) -> list:
        leaderboard = []
        for i, card in enumerate(self.leaderboard):
            leaderboard.append(
                f"{i + 1}. {card.name} - Rating: {card.calculate_rating()}"
                f"({card.record['wins']}-{card.record['losses']})"
            )
            print(leaderboard[i])
        return leaderboard

    def generate_tournament_report(self) -> dict:
        avg_rating = (
            sum(card.calculate_rating() for
                card in self.registered_cards.values())
            / len(self.registered_cards)
            if self.registered_cards
            else 0
        )
        report = {
            "total_cards": len(self.registered_cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active" if
            self.registered_cards else "not active",
        }
        return report
