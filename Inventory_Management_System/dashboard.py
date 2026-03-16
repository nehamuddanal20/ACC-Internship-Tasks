import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Neha@2024",
    database="inventory_db"
)

query = "SELECT * FROM inventory"
df = pd.read_sql(query, conn)

st.title("Inventory Management Dashboard")

st.subheader("Inventory Table")
st.dataframe(df)

st.subheader("Stock Quantity Chart")

fig, ax = plt.subplots()
ax.bar(df['item_name'], df['quantity'])
plt.xticks(rotation=45)

st.pyplot(fig)

st.subheader("Low Stock Items")

low_stock = df[df['quantity'] < df['reorder_level']]
st.write(low_stock)