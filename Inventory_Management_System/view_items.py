from database import cursor

def view_items():
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()

    print("\nInventory List\n")

    for row in rows:
        print("ID:", row[0])
        print("Item:", row[1])
        print("Quantity:", row[2])
        print("Price:", row[3])
        print("Reorder Level:", row[4])
        print("----------------------")


def low_stock_alert():
    cursor.execute("SELECT item_name, quantity, reorder_level FROM inventory")
    rows = cursor.fetchall()

    print("\nLow Stock Alerts\n")

    for row in rows:
        if row[1] < row[2]:
            print(f"ALERT: {row[0]} stock is low ({row[1]} items left)")