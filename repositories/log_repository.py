class LogRepository:
    def __init__(self,conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Log(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        action TEXT NOT NULL,
        description TEXT NOT NULL,
        timestamp TEXT NOT NULL
        )''')
        self.conn.commit()

    def save (self, user_id, action, description, time):
        self.cursor.execute('''INSERT INTO Log(USER_ID,ACTION,DESCRIPTION,TIMESTAMP)VALUES (?,?,?,?)''', (user_id,action,description,time))
        self.conn.commit()

    def find_all(self):
        self.cursor.execute('''SELECT * FROM Log''')
        return self.cursor.fetchall()

    def find_by_id(self, id):
        self.cursor.execute('''SELECT * FROM Log WHERE ID=?''', (id,))
        return self.cursor.fetchone()
