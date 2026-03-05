from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        artifacts, key=lambda power: power['power'], reverse=True
    )


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda prefix: "* " + prefix + " *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        'max_power': max(mages, key=lambda p: p['power']),
        'min_power': min(mages, key=lambda p: p['power']),
        'avg_power': round(sum(mage['power'] for mage in filter(
            lambda m: 'power' in m, mages)) / len(mages) if mages else 0, 2)
    }


def main() -> None:
    try:
        artifacts = [
            {"name": "Fire Staff", "power": 92, "type": "staff"},
            {"name": "Crystal Orb", "power": 85, "type": "orb"},
            {"name": "Shadow Cloak", "power": 60, "type": "cloak"},
        ]
        mages = [
            {"name": "Pate", "power": 10},
            {"name": "Bearer of the curse", "power": 99},
            {"name": "Gwyn, lord of cinder", "power": 100},
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
        print(f"Average power: {stats['avg_power']}")
    except Exception as e:
        print(f"Error: {e.__class__.__name__} - {e}")


if __name__ == "__main__":
    main()
