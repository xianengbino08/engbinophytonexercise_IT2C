from display_menu import display_menu
from take_orders import take_orders
from print_receipt import print_receipt


def main():
    display_menu()

    want_to_order = input("\nWould you like to order? (yes/no): ")

    if want_to_order == "yes":
        take_orders()
        print_receipt()
    else:
        print("Thank you for visiting! Goodbye.")


main()
