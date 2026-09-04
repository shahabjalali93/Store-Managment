from repositories.database import get_connection, create_tables
from views.product_view import ProductView
from tkinter import *

conn = get_connection('data/store.db')
create_tables(conn)

root = Tk()
ProductView(root, conn, (1, 'admin', '1234'))
root.mainloop()