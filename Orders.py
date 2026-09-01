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
