def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        if quantity < 0:
            print("negative value")
        seed_type = seed_type.capitalize()
        print(f"{seed_type} seeds: {quantity} {unit} available")
    elif unit == "grams":
        if quantity < 0:
            print("negative value")
        seed_type = seed_type.capitalize()
        print(f"{seed_type} seeds: {quantity} {unit} total")
    elif unit == "area":
        if quantity < 0:
            print("negative value")
        seed_type = seed_type.capitalize()
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
