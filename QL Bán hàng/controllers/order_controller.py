from config.db import get_connection

def create_order(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders(customer_id) VALUES (%s)", (customer_id,))
    conn.commit()
    order_id = cursor.lastrowid
    conn.close()
    return order_id

def add_order_detail(order_id, product_id, quantity, price):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """INSERT INTO order_details(order_id, product_id, quantity, price)
             VALUES (%s,%s,%s,%s)"""
    cursor.execute(sql, (order_id, product_id, quantity, price))
    conn.commit()
    conn.close()

def get_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT o.id, c.name as customer,
        SUM(od.quantity * od.price) as total
        FROM orders o
        JOIN customers c ON o.customer_id = c.id
        JOIN order_details od ON o.id = od.order_id
        GROUP BY o.id
    """)
    result = cursor.fetchall()
    conn.close()
    return result