def ft_harvest_total() -> None:
    x: int = 1
    total: int = 0
    while (x <= 3):
        d1: int = int(input(f"Day {x} harvest: "))
        x += 1
        total += d1
    print("Total harvest: ", total)
