class UserRepository:
    def __init__(self,conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME TEXT NOT NULL UNIQUE,
        PASSWORD TEXT NOT NULL)
        ''')
        self.conn.commit()

    def save (self,username,password):
        self.cursor.execute('''INSERT INTO user



 (USERNAME, PASSWORD)VALUES (?,?)''',(username,password))
        self.conn.commit()

    def find_by_username(self,username):
        self.cursor.execute('''SELECT *FROM user



 WHERE USERNAME = ?''',(username,))
        return self.cursor.fetchone()

    def find_by_id(self,id):
        self.cursor.execute('''SELECT *FROM user WHERE ID = ?''',(id,))
        return self.cursor.fetchone()

    def find_all(self):
        self.cursor.execute('''SELECT *FROM user''')
        return self.cursor.fetchall()
