from database import conn, cursor

def add_item():
    name = input("Enter Item Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    reorder = int(input("Enter Reorder Level: "))

    sql = "INSERT INTO inventory (item_name, quantity, price, reorder_level) VALUES (%s,%s,%s,%s)"
    val = (name, quantity, price, reorder)

    cursor.execute(sql, val)
    conn.commit()

    print("Item Added Successfully")