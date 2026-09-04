from controllers.sale_controller import SalesController
from controllers.customer_controller import CustomerController
from controllers.product_controller import ProductController
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class SaleView :
    def __init__(self,parent,conn,user):
        self._parent = parent
        self._conn = conn
        self.user = user
        self.sales_controller = SalesController(conn)
        self.customer_controller = CustomerController(conn)
        self.product_controller = ProductController(conn)
        self._build_ui()
        self._load_combos()
        self._load_sales()

    def _build_ui(self):
        form_frame = Frame(self._parent)
        form_frame.pack(fill=X, padx=10, pady=10)
        form_frame.columnconfigure(1, weight=1)

        Label(form_frame, text="Customer").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.customer_var = StringVar()
        self.customer_combo = ttk.Combobox(form_frame, textvariable=self.customer_var)
        self.customer_combo.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

        Label(form_frame, text="Product").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.product_var = StringVar()
        self.product_combo = ttk.Combobox(form_frame, textvariable=self.product_var)
        self.product_combo.grid(row=1, column=1, sticky='ew', padx=5, pady=5)

        Label(form_frame, text="Quantity").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.quantity_var = IntVar()
        Entry(form_frame, textvariable=self.quantity_var, width=30, bg='white', fg='black').grid(row=2, column=1,
                                                                                                 sticky='ew', padx=5,
                                                                                                 pady=5)

        btn_frame = Frame(self._parent)
        btn_frame.pack(fill=X, padx=10, pady=5)
        Button(btn_frame, text="Register Sale", command=self._register).pack(side=LEFT, padx=3)
        Button(btn_frame, text="Clear", command=self._clear).pack(side=LEFT, padx=3)

        self.table = ttk.Treeview(self._parent,
                                  columns=("ID", "Customer", "Product", "Quantity", "Total", "Date"), show="headings")
        self.table.heading("ID", text="ID")
        self.table.heading("Customer", text="Customer")
        self.table.heading("Product", text="Product")
        self.table.heading("Quantity", text="Quantity")
        self.table.heading("Total", text="Total")
        self.table.heading("Date", text="Date")
        self.table.pack(fill=BOTH, expand=True, padx=10, pady=10)
    def _load_combos(self):
        success , customers =self.customer_controller.get_all_customers()
        if success:
            self.customer_combo["values"] = [f"{c[0]} - {c[1]}" for c in customers]
            self.customers = customers
        success , product =self.product_controller.get_all_products()
        if success:
            self.product_combo["values"] = [f"{p[0]} - {p[1]}" for p in product]
            self.product = product

    def _load_sales(self):
        for row in self.table.get_children():
            self.table.delete(row)
        success , sales = self.sales_controller.get_all_sales()
        if success:
            for sale in sales:
                self.table.insert("",END,values=sale)

    def _register(self):
        customer_idx = self.customer_combo.current()
        product_idx = self.product_combo.current()
        quantity = self.quantity_var.get()
        if customer_idx < 0 or product_idx < 0 :
            messagebox.showerror("Error",f"Please select a valid customer and product .")
            return
        customer_id =self.customers[customer_idx][0]
        product_id =self.product[product_idx][0]
        success , message = self.sales_controller.register_sale(self.user[0],customer_id,product_id,quantity)
        if success:
            messagebox.showinfo("Success", message)
            self._load_sales()
            self._clear()
        else:
            messagebox.showerror("Error",message)


    def _clear(self):
        self.customer_var.set("")
        self.product_var.set("")
        self.quantity_var.set(0)














