import sys

def fill_dict(args: list) -> dict:
    inventory = {}
    try:
        for ar in args:
            item, count = ar.split(':')
            count = int(count)
            inventory.update({item: count})
    except Exception:
        raise ValueError("Invalid data, use format item:count with count as integer")
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
    print(item[0])
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
        max_item_name = [for item in inventory if inventory[item] == max_item]
        min_item_name = [for item in inventory if inventory[item] == min_item]
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
    for item in inventory:
        if inventory[item] <= 1:
            

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
    except Exception as e:
        print(f"Error in inventory system: {e}")
        
if __name__ == "__main__":
    ft_inventory_system()