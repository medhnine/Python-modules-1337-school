"""Exercise 1: Score Cruncher.

Processes player scores and displays analytics.
"""
from sys import argv


def ft_score_analytics() -> None:
    """Analyze player scores and display statistics."""
    print("=== Player Score Analytics ===")
    if len(argv) <= 1:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return
    scores = []
    i = 1
    while (i < len(argv)):
        try:
            scores.append(int(argv[i]))
        except ValueError:
            print("invalid input, enter numeric values")
            return
        i += 1
    print(f"Scores processed: {scores}")
    total_players = len(argv) - 1
    print(f"Total players: {total_players}")
    print(f"Total score: {sum(scores)}")
    Average_score = sum(scores) / total_players
    print(f"Average score: {Average_score}")
    high_score = int(max(scores))
    print(f"High score: {high_score}")
    Low_score = int(min(scores))
    print(f"Low score: {Low_score}")
    score_range = high_score - Low_score
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    ft_score_analytics()
