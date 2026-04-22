"""Ancient Text Recovery Module.

Recovers and displays data from ancient archive fragments
stored in the Cyber Archives vault system.
"""

from typing import TextIO


def recover_ancient_text(filepath: str) -> None:
    """Recover and display text from an ancient archive fragment.

    Opens the specified file, reads its contents, and displays
    the recovered data with status messages.

    Args:
        filepath: Path to the ancient fragment file to recover.

    Raises:
        FileNotFoundError: If the archive fragment doesn't exist.
        OSError: If a system-level I/O error occurs.
    """
    data: TextIO | None = None
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
        print(f"Accessing Storage Vault: {filepath}")
        data = open(filepath, "r")
        result: str = data.read()
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(f"{result}\n")
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError as e:
        print(e)
    except OSError as e:
        print(f"Operating system error: {e}")
    finally:
        if data is not None:
            data.close()


if __name__ == "__main__":
    recover_ancient_text("ancient_fragment.txt")
