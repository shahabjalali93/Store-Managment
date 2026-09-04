class CustomerRepository:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS customer(
             ID INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,   
             phone TEXT NOT NULL UNIQUE
        )''')
        self.conn.commit()

    def save(self, name, phone):
        self.cursor.execute('''INSERT INTO customer(name , phone)VALUES (?,?)''', (name, phone))
        self.conn.commit()

    def find_by_id(self, id):
        self.cursor.execute('''SELECT *FROM customer WHERE ID = ?''', (id,))
        return self.cursor.fetchone()

    def find_all(self):
        self.cursor.execute('''SELECT *FROM customer''')
        return self.cursor.fetchall()

    def find_by_name(self, name):
        self.cursor.execute('''SELECT *FROM customer WHERE NAME LIKE ?''', (f'%{name}%',) )
        return self.cursor.fetchall()

    def find_by_phone(self, phone):
        self.cursor.execute('''SELECT *FROM customer WHERE PHONE = ?''', (phone,))
        return self.cursor.fetchone()

    def update(self, id, name, phone):
        self.cursor.execute('''UPDATE customer SET NAME = ?, PHONE = ? WHERE ID=?''', (name, phone,id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute('''DELETE FROM customer WHERE ID = ?''', (id,))
        self.conn.commit()
