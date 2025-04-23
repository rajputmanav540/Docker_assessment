import streamlit as st
import mysql.connector
import json

# Connect to MySQL container by container name (because they're on the same bridge network)
conn = mysql.connector.connect(
    host="mysql-db",
    user="myuser",
    password="rootpass",
    database="mydatabase"
)

cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT * FROM your_table_name")  # replace with your actual table
rows = cursor.fetchall()

# Display as JSON
st.title("MySQL Data")
st.json(json.dumps(rows, indent=2))

cursor.close()
conn.close()
