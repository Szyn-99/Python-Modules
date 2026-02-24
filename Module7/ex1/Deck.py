from ex0.Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop(0)
        else:
            raise IndexError("Deck is empty. Cannot draw a card.")

    def get_deck_stats(self) -> dict:
        deck_stats = {
            "total_cards": len(self.cards),
            "creatures": sum(1 for card in self.cards
                             if card.type == "Creature"),
            "spells": sum(1 for card in self.cards if card.type == "Spell"),
            "artifacts": sum(1 for card in self.cards
                             if card.type == "Artifact"),
        }
        unique_cards = set(card for card in self.cards)
        average_cost = (
            sum(card.cost for card in unique_cards) / len(unique_cards)
            if unique_cards
            else 0
        )
        deck_stats["avg_cost"] = f"{average_cost:.2f}"
        return deck_stats
