from menu_data import menu, orders


def print_receipt():
    print("\n=================RECEIPT=================")
    print(f"{'ITEM':<15}{'QTY':>5}{'PRICE':>10}{'SUBTOTAL':>12}")
    print("-" * 42)

    overall_total = 0

    for item_name in orders:
        quantity = orders[item_name]
        price_per_item = menu[item_name]
        subtotal = price_per_item * quantity
        overall_total = overall_total + subtotal

        print(f"{item_name:<15}{quantity:>5}{price_per_item:>10.2f}{subtotal:>12.2f}")

    print("-" * 42)
    print(f"{'TOTAL:':<30}{overall_total:>12.2f}")
    print("=" * 42)
