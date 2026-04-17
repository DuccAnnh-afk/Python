from config.db import get_connection

def get_all_customers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    result = cursor.fetchall()
    conn.close()
    return result

def add_customer(name, address, phone):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO customers(name, address, phone) VALUES (%s,%s,%s)"
    cursor.execute(sql, (name, address, phone))
    conn.commit()
    conn.close()