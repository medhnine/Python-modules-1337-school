def check_temperature(temp_str: str) -> int:
    """Validate a temperature value for agricultural use (0-40°C).

    Converts the input to an integer and checks whether it falls
    within the acceptable range for plant growth.

    Args:
        temp_str: The temperature value to validate (string or int).

    Returns:
        The validated temperature as an int if it is within range,
        or None if the input is not a valid number.

    Raises:
        ValueError: If the temperature is outside the 0-40°C range
                    (caught internally and printed).
    """
    try:
        print(f"Testing temperature: {temp_str}")
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return
    if 0 <= temp <= 40:
        print(f"Temperature {temp}°C is perfect for plants!\n")
        return temp
    elif temp < 0:
        try:
            raise ValueError(
                f"Error: {temp}°C is too cold for plants (min 0°C)\n"
            )
        except ValueError as e:
            print(e)
    elif temp > 40:
        try:
            raise ValueError(
                f"Error: {temp}°C is too hot for plants (max 40°C)\n"
            )
        except ValueError as e:
            print(e)


def test_temperature_input() -> None:
    """
    Run a series of tests on check_temperature to demonstrate error handling.

    Tests good input, non-numeric input, and extreme values to show that
    the program continues running after exceptions are handled.
    """

    print("=== Garden Temperature Checker ===\n")
    test = input("enter temp : ")
    check_temperature(test)
    # check_temperature(25)
    # check_temperature("abc")
    # check_temperature(100)
    # check_temperature(-50)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
