"""Exercise 5: Stream Wizard.

Demonstrates generators and for-in loops.
"""
import time
from typing import Generator


def game_event_stream(n_events: int) -> Generator:
    """Generator that yields game events one at a time."""
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    for i in range(n_events):
        player = players[i % len(players)]
        action = actions[i % len(actions)]
        level = (i * 7 + 5) % 20 + 1
        yield {
            "id": i + 1,
            "player": player,
            "level": level,
            "action": action,
        }


def ft_fibonacci(count: int) -> Generator:
    """Generator that yields the first 'count' Fibonacci numbers."""
    i = 0
    y = 1
    n_of_iter = 0
    while n_of_iter < count:
        yield i
        i, y = y, i + y
        n_of_iter += 1


def is_prime(number: int) -> int:
    """Check if a number is prime. Returns 1 if prime, 0 otherwise."""
    if number == 2:
        return 1
    temp = number - 1
    while True:
        if number % temp == 0:
            return 0
        elif temp == 2:
            break
        temp -= 1
    return 1


def prime_number(number: int) -> Generator:
    """Generator that yields the first 'number' prime numbers."""
    if number == 0 or number == 1:
        return 0
    x = 2
    count = 0
    while count <= number:
        if is_prime(x) == 1:
            yield x
            count += 1
        if count == number:
            return
        x += 1
    return 0


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    target_events = 1000
    total_events = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    start_time = time.time()

    for event in game_event_stream(target_events):
        total_events += 1
        if event["level"] >= 10:
            high_level += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        elif event["action"] == "leveled up":
            level_up_events += 1
        if total_events <= 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {event['level']}) {event['action']}"
            )
        elif total_events == 4:
            print("...")

    elapsed = time.time() - start_time

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {target_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}\n")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {elapsed:.3f} seconds\n")
    n_fibonacci = 10
    count = 0
    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    for i in ft_fibonacci(n_fibonacci):
        if count < n_fibonacci - 1:
            print(f"{i}, ", end="")
        else:
            print(f"{i}\n", end="")
        count += 1
    number = 5
    count = 1
    print("Prime numbers (first 5): ", end="")
    for i in prime_number(number):
        if i != 0:
            if count < number:
                print(f"{i}, ", end="")
            else:
                print(f"{i}\n", end="")
            count += 1
