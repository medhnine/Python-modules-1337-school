"""Archive Creation Module.

Creates and writes new archive entries to the Cyber Archives
vault system using write mode file operations.
"""

from typing import TextIO


def create_archive(filepath: str, content: str) -> None:
    """Create an archive file and write content to it.

    Opens the specified file in write mode ('w'), writes the
    provided content, and ensures the file is properly closed.

    Args:
        filepath: Path to the archive file to create/overwrite.
        content: The data to write into the archive.

    Raises:
        OSError: If a system-level I/O error occurs.
    """
    file: TextIO | None = None
    try:
        print("=== CYBER ARCHIVES - ARCHIVE CREATION SYSTEM ===\n")
        print(f"Accessing Storage Vault: {filepath}")
        file = open(filepath, "w")
        file.write(content)
        print("Connection established...\n")
        print("Inscribing preservation data...")
        print(f"{content}\n")
        print("Data inscription complete. Storage unit sealed.")
    except Exception as e:
        print(e)
    finally:
        if file is not None:
            file.close()


if __name__ == "__main__":
    data: str = (
        "[ENTRY 001] New quantum algorithm discovered\n"
        "[ENTRY 002] Efficiency increased by 347%\n"
        "[ENTRY 003] Archived by Data Archivist trainee"
    )
    create_archive("output.txt", data)
