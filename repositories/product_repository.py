
import sqlite3

class ProductRepository:
    def __init__(self, repository):
        self.repository = repository
        self.cursor = self.repository.cursor()

    def create_table(self):

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS product (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                            NAME TEXT ,
                            CATEGORY TEXT, 
                            PRICE REAL ,
                            STOCK INTEGER 
         )
        ''')
        self.repository.commit()

    def save ( self, name, category, price, stock):
        self.cursor.execute('INSERT INTO product (name,category,price,stock) VALUES(?,?,?,?)',
                            (name,category,price,stock))

            
                            
        self.repository.commit()

    def find_all ( self ):
        cursor = self.repository.cursor()
        cursor.execute ('''SELECT * FROM product''')
        return cursor.fetchall()

    def find_by_id( self, id ):
        cursor = self.repository.cursor()
        cursor.execute ('''SELECT * FROM product WHERE id = ?''', (id,))
        return cursor.fetchone()

    def find_by_name(self, name):
        self.cursor.execute(
            '''SELECT * FROM product WHERE name LIKE ?''',
            (f'%{name}%',)
        )
        return self.cursor.fetchall()

    def delete ( self,id):
        self.cursor.execute('''DELETE FROM product WHERE id = ?''', (id,))
        self.repository.commit()

    def update( self, id, name, category, price, stock):
        self.cursor.execute('''UPDATE product SET name=?,category=?,price=?,stock=? WHERE id=? 
        ''', (name,category,price,stock,id))
        self.repository.commit()

    def update_stock(self, product_id, quantity):
        self.cursor.execute(
            'UPDATE product SET stock = stock - ? WHERE id = ?',
            (quantity, product_id)
        )
        self.repository.commit()