import sqlite3

def get_db_connection():

    db_connection = sqlite3.connect("src/data/hiscores.db")
    db_connection.isolation_level = None

    return db_connection

def initialize_database():

    connection = get_db_connection()
    create_table(connection)

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                    Hiscores (username TEXT, score INTEGER, status INTEGER);''')

    connection.commit()
