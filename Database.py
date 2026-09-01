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
