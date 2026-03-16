from database import conn, cursor

def update_stock():
    id = int(input("Enter Item ID: "))
    quantity = int(input("Enter New Quantity: "))

    sql = "UPDATE inventory SET quantity=%s WHERE id=%s"
    val = (quantity, id)

    cursor.execute(sql, val)
    conn.commit()

    print("Stock Updated")