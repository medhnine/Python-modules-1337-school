def ft_plot_area() -> None:
    length: int = int(input("Enter length: "))
    width: int = int(input("Enter width: "))
    if (width < 0 or length < 0):
        return
    result: int = length * width
    print("Plot area: ", result)
