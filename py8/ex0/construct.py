import sys
import os
import site


def is_venv() -> bool:
    """
    Returns True if running inside a virtual environment.
    sys.base_prefix is always the global Python root.
    sys.prefix changes to the venv root when activated.
    """
    return sys.prefix != sys.base_prefix


if __name__ == "__main__":
    if is_venv():
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {os.environ.get('VIRTUAL_ENV')}\n")

        print("SUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting\n"
              "the global system.")
        print()
        # the site-packages directory of the active environment.
        pack_path = site.getsitepackages()[0]
        print(f"Package installation path:\n{pack_path}")

    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment:  None detected\n")

        print("WARNING: You're in the global environment!\n"
              "The machines can see everything you install\n")

        print("To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
