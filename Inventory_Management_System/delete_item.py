from database import conn, cursor

def delete_item():
    id = int(input("Enter Item ID to Delete: "))

    sql = "DELETE FROM inventory WHERE id=%s"
    val = (id,)

    cursor.execute(sql, val)
    conn.commit()

    print("Item Deleted")