import sys

def extract_format(to_format: list) -> list:
    scores = []
    for i in to_format:
        try:
            score = int(i)
            scores += [score]
        except ValueError:
            raise ValueError("Invalid data, only integers acceptable")

    return scores

def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    try:
        if(len(sys.argv) < 2):
            raise Exception("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        scores = extract_format(sys.argv[1:])
        total_p = len(scores)
        total_s = sum(scores, 0)
        average_s = total_s / total_p
        max_s = max(scores)
        min_s = min(scores)
        range_s = max_s - min_s
        print(f"Scores processed: {scores}")
        print(f"Total players: {total_p}")
        print(f"Total score: {total_s}")
        print(f"Average score: {average_s}")
        print(f"High score: {max_s}")
        print(f"Low score: {min_s}")
        print(f"Score range: {range_s}")
    except Exception as e:
        print(e)
if __name__ == "__main__":
    ft_score_analytics()