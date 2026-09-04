from tkinter import *

class MainView:
    def __init__(self,conn,user):
        self.conn = conn
        self.user = user
        self.win = Tk()
        self.win.title("Store")
        self.win.geometry("600x600")
        self._build_ui()
        self.win.mainloop()

    def _build_ui(self):
        nav_frame = Frame(self.win , bg = "Navy")
        nav_frame.pack(side = TOP , fill = X)
        Button(nav_frame,text="Products", command=self._show_products).pack(side=LEFT , padx= 5, pady=5)
        Button(nav_frame,text="Customers", command=self._show_customers).pack(side=LEFT , padx= 5, pady=5)
        Button(nav_frame,text="Sales",command=self._show_sales).pack(side=LEFT , padx= 5, pady=5)
        Button(nav_frame,text="logs",command=self._show_logs).pack(side=LEFT , padx= 5, pady=5)
        Button(nav_frame,text="Logout",command=self._logout).pack(side=LEFT , padx= 5, pady=5)
        self.content_frame = Frame(self.win)
        self.content_frame.pack(fill= BOTH , expand= True)

    def _clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def _show_products(self):

            self._clear_content()
            try:
                from views.product_view import ProductView
                ProductView(self.content_frame, self.conn, self.user)
            except Exception as e:
                from tkinter import messagebox
                messagebox.showerror("Error", str(e))

    def _show_customers(self):
        self._clear_content()
        from views.customer_view import CustomerView
        CustomerView(self.content_frame,self.conn,self.user)

    def _show_sales(self):
        self._clear_content()
        from views.sale_view import SaleView
        SaleView(self.content_frame,self.conn,self.user)

    def _show_logs(self):
        self._clear_content()
        from views.log_view import LogView
        LogView(self.content_frame,self.conn)

    def _logout(self):
        self.win.destroy()











