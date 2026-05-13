def ft_do(number: int, start: int) -> None:
    if (start == (number + 1)):
        print("Harvest time!")
        return
    else:
        print("Day", start)
    start += 1
    ft_do(number, start)


def ft_count_harvest_recursive():
    number = int(input("Days until harvest: "))
    if (number < 0):
        return
    ft_do(number, 1)
