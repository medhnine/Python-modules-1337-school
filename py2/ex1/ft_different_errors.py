def garden_operations(
    value: str,
    elments: dict,
    number: int,
    file_name: str
) -> None:
    """Demonstrate different built-in exception types."""
    try:
        print("Testing ValueError...")
        int(value)
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        _ = number / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFoundError...")
        open(file_name)
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    try:
        print("Testing KeyError...")
        print(
            elments["missing_plant"]
        )
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")
    print("Testing multiple errors together...")
    try:
        int(value)
        _ = number / 0
        open(file_name)
        print(
            elments["missing_plant"]
        )
    except (
        ValueError,
        ZeroDivisionError,
        FileNotFoundError,
        KeyError,
    ):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    """Test garden_operations with inputs that trigger each error type."""
    print("=== Garden Error Types Demo ===\n")
    value = "abc"
    c = {"rose": 5}
    garden_operations(value, c, 8, "missing.txt")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
