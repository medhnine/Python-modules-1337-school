def ft_count_harvest_iterative() -> None:
    start = 1
    days = int(input("Days until harvest: "))
    while (start <= days):
        print("Day", start)
        start += 1
    if days >= 0:
        print("Harvest time!")
