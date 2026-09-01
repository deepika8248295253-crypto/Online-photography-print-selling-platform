from database import get_connection
def get_products():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT
            id,
            name,
            description,
            price,
            image_url
        FROM products
        ORDER BY id DESC
    """)
    products = cursor.fetchall()
    connection.close()
    return products
def add_product(
    name,
    description,
    price,
    image_url
):
    connection = get_connection()
    connection.execute("""
        INSERT INTO products
        (name, description, price, image_url)
        VALUES (?, ?, ?, ?)
    """, (
        name,
        description,
        price,
        image_url
    ))
    connection.commit()
    connection.close()
