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
