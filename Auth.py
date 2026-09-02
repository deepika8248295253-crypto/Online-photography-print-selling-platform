from database import get_connection
def register(username, password):
    if username == "" or password == "":
        return False, "Username and password required"
    connection = get_connection()
    try:
