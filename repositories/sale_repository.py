class SalesRepository:
    def __init__(self,conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def creat_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Sales (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,    
        USER_ID INTEGER NOT NULL,
        COSTUMER_ID INTEGER NOT NULL,
        PRODUCT_ID INTEGER NOT NULL,
        QUANTITY INTEGER NOT NULL,
        TOTAL REAL NOT NULL,
        DATE TEXT NOT NULL)''')
        self.conn.commit()

    def save (self,user_id,costumer_id,product_id,quantity,total,date):
        self.cursor.execute('''INSERT INTO Sales(USER_ID ,COSTUMER_ID,PRODUCT_ID,QUANTITY,TOTAL,DATE)VALUES (?,?,?,?,?,?)''', (user_id,costumer_id,product_id,quantity,total,date))
        self.conn.commit()

    def find_all(self):
        self.cursor.execute("""SELECT *FROM Sales """)
        return self.cursor.fetchall()

    
    def find_by_id(self, id):
        self.cursor.execute('''SELECT *FROM Sales WHERE ID=?''', (id,))
        return self.cursor.fetchone()

    def find_by_costumer(self, costumer_id):
        self.cursor.execute('''SELECT *FROM Sales WHERE COSTUMER_ID=?''', (costumer_id,))
        return self.cursor.fetchall()

    def find_by_product(self, product_id):
        self.cursor.execute('''SELECT *FROM Sales WHERE PRODUCT_ID=?''', (product_id,))
        return self.cursor.fetchall()

