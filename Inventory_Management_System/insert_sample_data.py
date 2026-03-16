import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Neha@2024",
    database="inventory_db"
)

cursor = conn.cursor()

data = [
("Monitor",15,12000,4),
("Printer",8,9000,2),
("USB Cable",100,150,20),
("Hard Disk",25,4500,6),
("RAM",20,3500,5),
("Router",12,2500,3),
("Webcam",18,2000,4),
("Headphones",40,1200,8),
("Speakers",22,2200,6),
("SSD",14,6000,3),
("Graphics Card",5,35000,2),
("Power Bank",35,1800,7),
("Laptop Stand",28,900,5),
("Cooling Pad",16,1300,4),
("Microphone",19,2700,4),
("Extension Board",45,700,10),
("Bluetooth Adapter",60,400,12)
]

sql = "INSERT INTO inventory (item_name, quantity, price, reorder_level) VALUES (%s,%s,%s,%s)"

cursor.executemany(sql, data)

conn.commit()

print("Sample data inserted successfully!")