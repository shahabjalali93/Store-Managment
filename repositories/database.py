import sqlite3
import os
def get_connection(db_path):
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect(db_path)
    return conn

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS product(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        price REAL,
        stock INTEGER
        )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales(  
        ID INTEGER PRIMARY KEY AUTOINCREMENT,    
        USER_ID INTEGER NOT NULL,
        COSTUMER_ID INTEGER NOT NULL,
        PRODUCT_ID INTEGER NOT NULL,
        QUANTITY INTEGER NOT NULL,
        TOTAL REAL NOT NULL,
        DATE TEXT NOT NULL
        )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS user(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME TEXT NOT NULL UNIQUE,
        PASSWORD TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS customer(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,   
        PHONE TEXT NOT NULL UNIQUE)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS log(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        action TEXT NOT NULL,
        description TEXT NOT NULL,
        timestamp TEXT NOT NULL)''')
    conn.commit()
