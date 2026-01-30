import sys


def fill_dict(args: list) -> dict:
    inventory = {}
    try:
        for ar in args:
            item, count = ar.split(":")
            count = int(count)
            inventory.update({item: count})
    except Exception:
        raise ValueError(
            "Invalid data, use format item:count with count as integer"
        )
    return inventory


def show_stats(inventory: dict, inv_items_total: int) -> None:
    print("=== Current Inventory ===")
    try:
        for item in inventory:
            """part / whole x 100 = percentage"""
            percent = inventory[item] / inv_items_total * 100
            print(f"{item}: {inventory[item]} units ({percent:.1f}%)")
        print()
    except Exception:
        raise


def get_name(item: list) -> str:
    name = ""
    for c in item:
        if c == "'" or c == "[" or c == "]":
            continue
        elif c == ",":
            return name
        name += c

    return name


def show_more_stats(inventory: dict) -> None:
    print("=== Inventory Statistics ===")
    try:
        max_item = max(inventory.values())
        min_item = min(inventory.values())
        max_item_name = [
            item for item in inventory if inventory[item] == max_item
        ]
        min_item_name = [
            item for item in inventory if inventory[item] == min_item
        ]
        if max_item == min_item:
            min_item_name = None
            min_item = 0
        else:
            min_item_name = min_item_name[0]
        print(f"Most abundant: {max_item_name[0]} ({max_item} units)")
        print(f"Least abundant: {min_item_name} ({min_item} units)")
    except Exception:
        raise


def restock_reminder(inventory: dict) -> None:
    print("\n=== Management Suggestions ===")
    restock = [item for item in inventory if inventory[item] <= 1]
    print(f"Restock needed: {restock}")


def sample_lookup(inventory: dict, item: str) -> None:
    if item is not None and item in inventory:
        print(f"Sample lookup - '{item}' in inventory: True")
    else:
        print(f"Sample lookup - '{item}' in inventory: False")


def item_categories(inventory: dict, inv_items_total: int) -> None:
    print("\n=== Item Categories ===")
    cat = {"moderate": {}, "scarce": {}}
    for item in inventory:
        percent = inventory[item] / inv_items_total * 100
        if percent >= 40:
            cat["moderate"].update({item: inventory[item]})
        else:
            cat["scarce"].update({item: inventory[item]})
    print(f"Moderate: {cat['moderate']}")
    print(f"Scarce: {cat['scarce']}")


def dictionary_properties(inventory: dict) -> None:
    print("\n=== Dictionary Properties Demo ===")

    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary Values: {list(inventory.values())}")


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    try:
        arguments = sys.argv[1:]
        inventory = fill_dict(arguments)
        inv_items_total = sum(inventory.values())
        inv_items_unique = len(inventory)
        print(f"Total items in inventory: {inv_items_total}")
        print(f"Unique item types: {inv_items_unique}\n")
        show_stats(inventory, inv_items_total)
        show_more_stats(inventory)
        item_categories(inventory, inv_items_total)
        restock_reminder(inventory)
        dictionary_properties(inventory)
        sample_lookup(inventory, "helmet")
    except Exception as e:
        print(f"Error in inventory system: {e}")


if __name__ == "__main__":
    ft_inventory_system()
