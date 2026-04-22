"""Exercise 3: Achievement Hunter.

Demonstrates set operations for achievement tracking.
"""


def Achievement_analytics(
    player1: set, player2: set, player3: set
) -> None:
    """Analyze achievements using set operations."""
    print("=== Achievement Analytics ===")
    unique_achievements = set.union(player1, player2, player3)
    common = set.intersection(player1, player2, player3)

    alice_only = player1.difference(player2, player3)
    bob_only = player2.difference(player1, player3)
    charlie_only = player3.difference(player1, player2)
    rare = alice_only.union(bob_only, charlie_only)
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}\n")
    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {rare}\n")
    print(f"Alice vs Bob common: {set.intersection(player2, player1)}")
    print(f"Alice unique: {set.difference(player1, player2)}")
    print(f"Bob unique: {set.difference(player2, player1)}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    Alice = {
        'first_kill', 'level_10',
        'treasure_hunter', 'speed_demon'
    }
    print(f"Player alice achievements: {Alice}")
    Bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    print(f"Player Bob achievements: {Bob}")
    Charlie = {
        'level_10', 'treasure_hunter', 'boss_slayer',
        'speed_demon', 'perfectionist'
    }
    print(f"Player Charlie achievements: {Charlie}\n")
    Achievement_analytics(Alice, Bob, Charlie)
