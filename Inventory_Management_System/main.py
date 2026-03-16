from add_item import add_item
from view_items import view_items, low_stock_alert
from update_stock import update_stock
from delete_item import delete_item

while True:

    print("\nInventory Management System")
    print("1 Add Item")
    print("2 View Items")
    print("3 Update Stock")
    print("4 Delete Item")
    print("5 Low Stock Alert")
    print("6 Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        view_items()

    elif choice == "3":
        update_stock()

    elif choice == "4":
        delete_item()

    elif choice == "5":
        low_stock_alert()

    elif choice == "6":
        break

    else:
        print("Invalid Choice")