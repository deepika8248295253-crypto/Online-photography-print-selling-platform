from database import get_connection
def place_order(
    username,
    product_name,
    quantity,
    total
):
    connection = get_connection()
    connection.execute("""
        INSERT INTO orders
        (username, product_name, quantity, total)
        VALUES (?, ?, ?, ?)
    """, (
        username,
        product_name,
        quantity,
        total
    ))
    connection.commit()
    connection.close()
    def get_orders(username=None):
    connection = get_connection()
    cursor = connection.cursor()

    if username:
        cursor.execute("""
            SELECT
                id,
                username,
                product_name,
                quantity,
                total,
                status
            FROM orders
            WHERE username=?
            ORDER BY id DESC
        """, (username,))
    else:
        cursor.execute("""
            SELECT
                id,
                username,
                product_name,
                quantity,
                total,
                status
            FROM orders
            ORDER BY id DESC
        """)
    orders = cursor.fetchall()
    connection.close()
    return orders
    def update_status(
    order_id,
    status
):
    connection = get_connection()
    connection.execute("""
        UPDATE orders
        SET status=?
        WHERE id=?
    """, (
        status,
        order_id
    ))
    connection.commit()
    connection.close()
