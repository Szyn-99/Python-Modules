def generate_data() -> dict:
    return {
        "Szyn": {
            "Achievements": [
                "first_kill",
                "level_99",
                "boss_slayer",
                "collector",
                "speed_runner",
                "fashionista",
                "DarkLord",
                "MasterExplorer",
                "UltimateChampion",
            ],
            "Total Score": 9999,
            "Active": True,
            "Region": "East",
        },
        "Solaire": {
            "Achievements": [
                "Sharp Shooter",
                "Marathon Runner",
                "boss_slayer",
                "level_10",
                "speed_demon",
                "treasure_hunter",
                "Sun Seeker",
                "Praiser of The Sun",
            ],
            "Total Score": 10000,
            "Active": True,
            "Region": "North",
        },
        "Alice": {
            "Achievements": [
                "First Kill",
                "Sharp Shooter",
                "Marathon Runner",
                "boss_slayer",
                "level_10",
                "speed_demon",
                "treasure_hunter",
            ],
            "Total Score": 2824,
            "Active": True,
            "Region": "North",
        },
        "Bob": {
            "Achievements": [
                "first_kill",
                "level_10",
                "boss_slayer",
                "collector",
                "speed_runner",
                "fashionista",
            ],
            "Total Score": 1500,
            "Active": False,
            "Region": "West",
        },
        "Charlie": {
            "Achievements": [
                "first_kill",
                "level_10",
                "boss_slayer",
                "speed_demon",
                "collector",
                "speed_runner",
            ],
            "Total Score": 1000,
            "Active": True,
            "Region": "South",
        },
        "Diana": {
            "Achievements": [
                "level_10",
                "boss_slayer",
                "speed_demon",
                "collector",
                "speed_runner",
            ],
            "Total Score": 500,
            "Active": True,
            "Region": "North",
        },
    }


def comprehension_l(game_data: dict) -> None:
    high_score = [
        player for player in game_data
        if game_data[player]["Total Score"] > 2000
    ]
    double_score = [
        game_data[player]["Total Score"] * 2 for player in game_data
    ]
    active_players = [
        player for player in game_data if game_data[player]["Active"] is True
    ]
    print(f"High scorers (>2000): {high_score}")
    print(f"Scores doubled: {double_score}")
    print(f"Active players: {active_players}")


def comprehension_d(game_data: dict) -> None:
    players_scores = {
        score: game_data[score]["Total Score"] for score in game_data
    }
    score_cat = {
        "high": sum(
            1 for high in game_data if game_data[high]["Total Score"] > 1500
        ),
        "medium": sum(
            1
            for high in game_data
            if game_data[high]["Total Score"] <= 1500
            and game_data[high]["Total Score"] >= 1000
        ),
        "low": sum(
            1 for high in game_data if game_data[high]["Total Score"] <= 500
        ),
    }
    achievement_counts = {
        player: len(game_data[player]["Achievements"])
        for player in game_data
    }

    print(f"Player scores: {players_scores}")
    print(f"Score categories: {score_cat}")
    print(f"Achievement counts: {achievement_counts}")


def comprehension_s(game_data: dict) -> None:
    unqiue_p = {player for player in game_data}
    unqiue_a = {
        achievement
        for player in game_data
        for achievement in game_data[player]["Achievements"]
    }
    active_regions = {
        game_data[player]["Region"]
        for player in game_data
        if game_data[player]["Active"]
    }
    print(f"Unique players: {unqiue_p}")
    print(f"Unique achievements: {unqiue_a}")
    print(f"Active regions: {active_regions}")


def extra_status(game_data: dict) -> tuple:
    total_p = sum(1 for player in game_data)
    unique_achievements = {
        ach for player in game_data
        for ach in game_data[player]["Achievements"]
    }
    total_unique_ach = sum(1 for ach in unique_achievements)

    scores = []
    for player in game_data:
        scores += [game_data[player]["Total Score"]]
    best_performer = {"name": "", "score": 0, "achievements": 0}
    max_score = 0
    for player in game_data:
        if game_data[player]["Total Score"] > max_score:
            max_score = game_data[player]["Total Score"]
            best_performer["name"] = player
            best_performer["score"] = game_data[player]["Total Score"]
            best_performer["achievements"] = len(
                game_data[player]["Achievements"]
            )

    average_score = sum(scores) / len(scores)
    print(f"Total players: {total_p}")
    print(
        f"Total unique achievements: {total_unique_ach}"
    )
    print(f"Average score: {average_score:.1f}")
    print(
        f"Top performer: {best_performer['name']} "
        f"({best_performer['score']} points, "
        f"{best_performer['achievements']} achievements)"
    )


def combined_analysis() -> None:
    try:
        game_data = generate_data()
        print("=== Game Analytics Dashboard ===")
        print("\n=== List Comprehension Examples ===")
        comprehension_l(game_data)
        print("\n=== Dict Comprehension Examples ===")
        comprehension_d(game_data)
        print("\n=== Set Comprehension Examples ===")
        comprehension_s(game_data)
        print("\n=== Combined Analysis ===")
        extra_status(game_data)
    except Exception as e:
        print("Something went wrong :(")
        print(f"Error Details : {e}")


if __name__ == "__main__":
    combined_analysis()
