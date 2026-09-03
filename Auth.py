from database import get_connection
def register(username, password):
    if username == "" or password == "":
        return False, "Username and password required"
    connection = get_connection()
    try:
        connection.execute("""
            INSERT INTO users
            (username, password, role)
            VALUES (?, ?, ?)
        """, (
            username,
            password,
            "customer"
        ))
        connection.commit()
        return True, "Registration successful"
        except:
        return False, "Username already exists"
    finally:
        connection.close()
        def login(username, password):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT username, role
        FROM users
        WHERE username=?
        AND password=?
    """, (
        username,
        password
    ))
user = cursor.fetchone()
    connection.close()
    return user
