from menu_data import menu


def display_menu():
    print("\n" + "*" * 40)
    print("*" + "MENU".center(38) + "*")
    print("*" * 40)
    print(f"|{'ITEM':<25}{'PRICE (PHP)':>13}|")
    print("|" + "-" * 38 + "|")

    for item in menu:
        price = menu[item]
        print(f"|{item:<25}{price:>13.2f}|")

    print("|" + "-" * 38 + "|")
    print("*" * 40)
