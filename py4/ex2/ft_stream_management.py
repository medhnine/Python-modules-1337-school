import sys

if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
        sys.stdout.write("Input Stream active. Enter archivist ID: ")
        sys.stdout.flush()
        data = input()
        sys.stdout.write("Input Stream active. Enter status report: ")
        sys.stdout.flush()
        data2 = input()
        sys.stdout.write(
            f"\n[STANDARD] Archive status from {data}"
            f": {data2}\n"
        )
        sys.stderr.write(
            "[ALERT] System diagnostic:"
            " Communication channels verified\n"
        )
        sys.stdout.write("[STANDARD] Data transmission complete\n")
        sys.stdout.write(
            "\nThree-channel communication test successful.\n"
        )
    except Exception as e:
        print(e)
