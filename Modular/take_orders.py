from menu_data import menu, orders


def take_orders():
    ordering = True

    while ordering == True:
        item_name = input("Enter menu item: ")
        item_name = item_name.title()

        if item_name in menu:
            try:
                quantity = int(input(f"Enter quantity for {item_name}: "))
                orders[item_name] = quantity
            except ValueError:
                print("Please enter a valid whole number.")
        else:
            print("Item not found in the menu. Please try again.")

        more = input("Do you want to order another item? (yes/no): ")

        if more == "no":
            ordering = False
