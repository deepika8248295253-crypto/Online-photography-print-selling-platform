import sqlite3
DATABASE = "photography.db"
def get_connection():
    return sqlite3.connect(
        DATABASE,
        check_same_thread=False
    )
def init_db():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            image_url TEXT
        )
    """)
    # ORDERS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            total REAL NOT NULL,
            status TEXT DEFAULT 'Placed'
        )
    """)
    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        ("admin",)
    )
    if cursor.fetchone() is None:
        cursor.execute("""
            INSERT INTO users
            (username, password, role)
            VALUES (?, ?, ?)
        """, (
            "admin",
            "admin123",
            "admin"
        ))
    cursor.execute(
        "SELECT COUNT(*) FROM products"
    )
    count = cursor.fetchone()[0]
    if count == 0:
        products = [
            (
                "Sunset Beach",
                "Beautiful sunset photography print",
                499,
                "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
            ),
            (
                "Mountain View",
                "Beautiful mountain photography print",
                699,
                "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b"
            ),
            (
                "Forest Nature",
                "Nature photography print",
                599,
                "https://images.unsplash.com/photo-1448375240586-882707db888b"
            )
        ]
        cursor.executemany("""
            INSERT INTO products
            (name, description, price, image_url)
            VALUES (?, ?, ?, ?)
        """, products)
    connection.commit()
    connection.close()
