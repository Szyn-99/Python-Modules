from typing import Iterator


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda power: power['power'], reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> Iterator[dict]:
    return filter(lambda mage: mage['power'] >= min_power, mages)


def spell_transformer(spells: list[str]) -> Iterator[str]:
    return map(lambda prefix: "*" + prefix + "*", spells)


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda p: p['power']),
        'min_power': min(mages, key=lambda p: p['power']),
        'avg_power': sum(mage['power'] for mage in mages) / len(mages)
    }


def main():
    try:
        artifacts = [
            {"name": "Fire Staff", "power": 92, "type": "staff"},
            {"name": "Crystal Orb", "power": 85, "type": "orb"},
            {"name": "Shadow Cloak", "power": 60, "type": "cloak"},
        ]
        mages = [
            {"name": "Gandalf", "power": 95},
            {"name": "Merlin", "power": 88},
            {"name": "Morgana", "power": 72},
        ]
        spells = ["fireball", "heal", "shield"]

        print("Testing artifact sorter...")
        sorted_artifacts = artifact_sorter(artifacts)
        for i in range(len(sorted_artifacts) - 1):
            curr = sorted_artifacts[i]
            nxt = sorted_artifacts[i + 1]
            print(
                f"{curr['name']} ({curr['power']} power) "
                f"comes before {nxt['name']} ({nxt['power']} power)"
            )

        print("\nTesting power filter...")
        filter_criteriaaaaa = 70
        filtered = list(power_filter(mages, filter_criteriaaaaa))
        for mage in filtered:
            print(
                f"{mage['name']} has {mage['power']} "
                f"power (>= {filter_criteriaaaaa})"
            )

        print("\nTesting spell transformer...")
        transformed = list(spell_transformer(spells))
        print(*transformed)

        print("\nTesting mage stats...")
        stats = mage_stats(mages)
        print(
            f"Most powerful: {stats['max_power']['name']}"
            f" ({stats['max_power']['power']} power)"
        )
        print(
            f"Least powerful: {stats['min_power']['name']}"
            f" ({stats['min_power']['power']} power)"
        )
        print(f"Average power: {stats['avg_power']:.1f}")
    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")


if __name__ == "__main__":
    main()
