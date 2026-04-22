class SecurePlant:
    """A plant with secure height and age attributes."""

    def __init__(self, name: str, height: int,
                 age: int) -> None:
        """Initialize a secure plant."""
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height, False)
        self.set_age(age, False)

    def set_height(self, number: int, display: bool) -> None:
        """Set plant height if value is valid."""
        if (number >= 0):
            if display is True:
                print(f"Height updated: {number}cm [OK]")
            self._height = number
        else:
            print(f"Invalid operation attempted: height {number}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, number: int, display: bool) -> None:
        """Set plant age if value is valid."""
        if (number >= 0):
            if number >= 3:
                if display is True:
                    print(f"Age updated: {number} days [OK]")
                self._age = number
            else:
                if display is True:
                    print(f"Age updated: {number} day [OK]")
                self._age = number
        else:
            print(f"Invalid operation attempted: age {number}cm [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        """Return the plant height."""
        return self._height

    def get_age(self) -> int:
        """Return the plant age."""
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = SecurePlant("Rose", 9, 14)
    print("Plant created: Rose")
    p1.set_height(25, True)
    p1.set_age(30, True)
    print()
    p1.set_height(-5, True)
    print(f"\nCurrent plant: Rose ({p1.get_height()}cm, {p1.get_age()} days)")
