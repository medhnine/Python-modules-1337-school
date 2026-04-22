"""Exercise 0: Command Quest.

Demonstrates command-line argument processing.
"""
from sys import argv


if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {argv[0]}")
    i = 1
    while (i < len(argv)):
        if i == 1:
            print(f"Arguments received: {len(argv) - 1}")
        print(f"Argument {i}: {argv[i]}")
        i += 1
    if i == 1:
        print("No arguments provided!")
    print(f"Total arguments: {len(argv)}")
