"""Exercise 4: Inventory Master.

Manages player inventories using nested dictionaries.
"""
from sys import argv


def ft_inventory_system() -> None:
    """Process inventory items and display analytics."""
    inventory = {}
    print("=== Inventory System Analysis ===")
    index = 1
    count = len(argv)
    if count == 1:
        print("no arguments")
        return
    try:
        while index < count:
            elements = argv[index].split(':')
            name = elements[0]
            qty = int(elements[1])
            inventory[name] = {'quantity': qty}
            index += 1
    except Exception as e:
        print(e)
        return
    print(inventory)
    sum_num = 0
    for key in inventory:
        sum_num += inventory[key]['quantity']
    print(f"Total items in inventory: {sum_num}")
    print(f"Unique item types: {len(inventory)}")

    for key in inventory:
        max_num = inventory[key]['quantity']
        min_num = inventory[key]['quantity']
        target = key
        target2 = key
        break
    for key in inventory:
        qty = inventory[key]['quantity']
        if qty > max_num:
            max_num = qty
            target = key
        if qty < min_num:
            min_num = qty
            target2 = key

    print("\n=== Current Inventory ===")
    for key in inventory:
        qty = inventory[key]['quantity']
        unit = "unit" if qty == 1 else "units"
        pct = (qty / sum_num) * 100
        print(f"{key}: {qty} {unit} ({pct:.1f}%)")

    print("\n=== Inventory Statistics ===")
    max_unit = "unit" if max_num == 1 else "units"
    min_unit = "unit" if min_num == 1 else "units"
    print(f"Most abundant: {target} ({max_num} {max_unit})")
    print(f"Least abundant: {target2} ({min_num} {min_unit})")

    print("=== Item Categories ===")
    Moderate = {target: inventory[target]['quantity']}
    print(f"Moderate: {Moderate}")
    scarce = {}
    for key in inventory:
        if key != target:
            scarce[key] = inventory[key]['quantity']
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    Restock = []
    for key in inventory:
        if inventory[key]['quantity'] == min_num:
            Restock.append(key)
    print(f"Restock needed: {', '.join(Restock)}")

    print("\n=== Dictionary Properties Demo ===")
    keys_str = ", ".join(inventory.keys())
    values_str = ", ".join(str(inventory[k]['quantity']) for k in inventory)
    print(f"Dictionary keys: {keys_str}")
    print(f"Dictionary values: {values_str}")
    print(f"Sample lookup - '{target}' in inventory: {target in inventory}")


if __name__ == "__main__":
    ft_inventory_system()
