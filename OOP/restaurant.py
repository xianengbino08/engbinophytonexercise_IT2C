class Restaurant:
    # __init__ creates the object and sets up its attributes
    def __init__(self):
        self.menu = {
            "Burger": 85.00,
            "Cheeseburger": 95.00,
            "Fries": 55.00,
            "Fried Chicken": 89.00,
            "Spaghetti": 65.00,
            "Soda": 35.00,
            "Iced Tea": 30.00,
            "Bottled Water": 20.00,
        }
        self.orders = {}

    # Methods = the behaviors of this object

    def display_menu(self):
        print("\n" + "*" * 40)
        print("*" + "MENU".center(38) + "*")
        print("*" * 40)
        print(f"|{'ITEM':<25}{'PRICE (PHP)':>13}|")
        print("|" + "-" * 38 + "|")

        for item in self.menu:
            price = self.menu[item]
            print(f"|{item:<25}{price:>13.2f}|")

        print("|" + "-" * 38 + "|")
        print("*" * 40)

    def take_orders(self):
        ordering = True

        while ordering == True:
            item_name = input("Enter menu item: ")
            item_name = item_name.title()

            if item_name in self.menu:
                try:
                    quantity = int(input(f"Enter quantity for {item_name}: "))
                    self.orders[item_name] = quantity
                except ValueError:
                    print("Please enter a valid whole number.")
            else:
                print("Item not found in the menu. Please try again.")

            more = input("Do you want to order another item? (yes/no): ")

            if more == "no":
                ordering = False

    def print_receipt(self):
        print("\n=================RECEIPT=================")
        print(f"{'ITEM':<15}{'QTY':>5}{'PRICE':>10}{'SUBTOTAL':>12}")
        print("-" * 42)

        overall_total = 0

        for item_name in self.orders:
            quantity = self.orders[item_name]
            price_per_item = self.menu[item_name]
            subtotal = price_per_item * quantity
            overall_total = overall_total + subtotal

            print(f"{item_name:<15}{quantity:>5}{price_per_item:>10.2f}{subtotal:>12.2f}")

        print("-" * 42)
        print(f"{'TOTAL:':<30}{overall_total:>12.2f}")
        print("=" * 42)

    def run(self):
        self.display_menu()

        want_to_order = input("\nWould you like to order? (yes/no): ")

        if want_to_order == "yes":
            self.take_orders()
            self.print_receipt()
        else:
            print("Thank you for visiting! Goodbye.")
