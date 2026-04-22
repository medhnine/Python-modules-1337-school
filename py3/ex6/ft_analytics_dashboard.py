"""Exercise 6: Data Alchemist.

Demonstrates all types of comprehensions.
"""


def list_comprehension(players: list) -> None:
    """Demonstrate list comprehensions."""
    print("=== List Comprehension Examples ===")
    high_players_scores = [
        x['name'] for x in players if x['score'] > 2000
    ]
    print(f"High scorers (>2000): {high_players_scores}")
    Scores_doubled = [x['score'] * 2 for x in players]
    print(f"Scores doubled: {Scores_doubled}")
    active_players = [x['name'] for x in players if x['status'] is True]
    print(f"Active players: {active_players}\n")


def dict_comprehension(players: list) -> None:
    """Demonstrate dictionary comprehensions."""
    print("=== Dict Comprehension Examples ===")
    players_scores = {
        x['name']: x['score']
        for x in players if x['status'] is True
    }
    print(f"Player scores: {players_scores}")
    players_with_high_score = [
        x['name'] for x in players if x['score'] > 2000
    ]
    medium_score = [
        x['name'] for x in players
        if 1000 < x['score'] < 2000
    ]
    low_score = [
        x['name'] for x in players if x['score'] <= 1000
    ]
    score_categories = {
        'high': len(players_with_high_score),
        'medium': len(medium_score),
        'low': len(low_score)
    }
    print(f"Score categories: {score_categories}")
    Achievement = {
        x['name']: len(x['achievement']) for x in players
    }
    print(f"Achievement counts: {Achievement}")


def set_comprehension(players: list) -> set:
    """Demonstrate set comprehensions."""
    print("\n=== Set Comprehension Examples ===")
    unique_players = {(x['name']) for x in players}
    print(f"Unique players: {unique_players}")
    unique_achievement = {
        achv for player in players
        for achv in player['achievement']
    }
    print(f"Unique achievements: {unique_achievement}")
    active_regions = {x['regions'] for x in players}
    print(f"Active regions: {active_regions}")
    return unique_achievement


def combined_analysis(
    players: list, unique_achievement: set
) -> None:
    """Combine comprehensions for analytics."""
    print("\n=== Combined Analysis ===")
    players_list = [x['name'] for x in players]
    print(f"Total players: {len(players_list)}")
    print(f"Total unique achievements: {len(unique_achievement)}")
    score_sum = 0
    score_sum += sum([x['score'] for x in players])
    print(f"Average score: {score_sum / len(players_list)}")
    performers = {
        x['name']: len(x['achievement']) for x in players
    }
    top_performer = max(performers, key=performers.get)
    number = [
        len(x['achievement'])
        for x in players if x['name'] == top_performer
    ]
    score = [
        x['score']
        for x in players if x['name'] == top_performer
    ]
    print(
        f"Top performer: {top_performer}"
        f" ({score[0]} points, {number[0]} achievements)"
    )


def ft_analytics_dashboard() -> None:
    """Run all comprehension demonstrations."""
    print("=== Game Analytics Dashboard ===\n")
    players = [
        {
            'name': 'alice', 'score': 2300,
            'status': True,
            'achievement': [
                'first_kill', 'level_10', 'boss_slayer'
            ],
            'regions': 'east'
        },
        {
            'name': 'charlie', 'score': 2100,
            'status': True,
            'achievement': ['first_kill', 'boss_slayer'],
            'regions': 'north'
        },
        {
            'name': 'diana', 'score': 1800,
            'status': True,
            'achievement': ['first_kill', 'boss_slayer'],
            'regions': 'north'
        },
        {
            'name': 'bob', 'score': 1600,
            'status': True,
            'achievement': ['level_10', 'boss_slayer'],
            'regions': 'east'
        },
        {
            'name': 'jhon', 'score': 1000,
            'status': False,
            'achievement': ['level_10', 'boss_slayer'],
            'regions': 'central'
        }
    ]

    list_comprehension(players)
    dict_comprehension(players)
    unique_achievement = set_comprehension(players)
    combined_analysis(players, unique_achievement)


ft_analytics_dashboard()
