from config.db import get_connection

def get_all_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    result = cursor.fetchall()
    conn.close()
    return result

def add_product(name, origin, price):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO products(name, origin, price) VALUES (%s,%s,%s)"
    cursor.execute(sql, (name, origin, price))
    conn.commit()
    conn.close()

def delete_product(pid):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=%s", (pid,))
    conn.commit()
    conn.close()