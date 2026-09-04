from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controllers.product_controller import ProductController
class ProductView :
    def __init__(self,parent,conn,user):
        self.parent = parent
        self.conn = conn
        self.user = user
        self.controller = ProductController(conn)
        self._build_ui()
        self._load_product()

    def _build_ui(self):

        form_frame = Frame(self.parent)
        form_frame.pack(fill=X, padx=10, pady=10)
        form_frame.columnconfigure(1, weight=1)

        Label(form_frame, text="Name").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.name_var = StringVar()
        Entry(form_frame, textvariable=self.name_var, width=30, bg='white', fg='black').grid(row=0, column=1,sticky='ew', padx=5,pady=5)

        Label(form_frame, text="Category").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.category_var = StringVar()
        Entry(form_frame, textvariable=self.category_var, width=30, bg='white', fg='black').grid(row=1, column=1, sticky='ew',padx=5, pady=5)

        Label(form_frame, text="Price").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.price_var = DoubleVar()
        Entry(form_frame, textvariable=self.price_var, width=30, bg='white', fg='black').grid(row=2, column=1,sticky='ew', padx=5,pady=5)

        Label(form_frame, text="Stock").grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.stock_var = IntVar()
        Entry(form_frame, textvariable=self.stock_var, width=30, bg='white', fg='black').grid(row=3, column=1,sticky='ew', padx=5,pady=5)

        btn_frame = Frame(self.parent)
        btn_frame.pack(fill=X, padx=10, pady=5)
        Button(btn_frame, text="Add", command=self._add).pack(side=LEFT, padx=3)
        Button(btn_frame, text="Update", command=self._update).pack(side=LEFT, padx=3)
        Button(btn_frame, text="Delete", command=self._delete).pack(side=LEFT, padx=3)
        Button(btn_frame, text="Search", command=self._search).pack(side=LEFT, padx=3)
        Button(btn_frame, text="Clear", command=self._clear).pack(side=LEFT, padx=3)

        self.table = ttk.Treeview(self.parent,
                                      columns=("id", "name", "category", "price", "stock"), show="headings")
        self.table.heading("id", text="ID")
        self.table.heading("name", text="Name")
        self.table.heading("category", text="Category")
        self.table.heading("price", text="Price")
        self.table.heading("stock", text="Stock")
        self.table.pack(fill=BOTH, expand=True, padx=10, pady=10)
        self.table.bind("<<TreeviewSelect>>", self._select)


    def _load_product(self):
        for row in self.table.get_children():
            self.table.delete(row)
        success , product = self.controller.get_all_products()
        if success:
            for p in product:
                self.table.insert("",END,values=p)

    def _clear(self):
        self.name_var.set("")
        self.category_var.set("")
        self.price_var.set(0)
        self.stock_var.set(0)

    def _select(self,event):
        selected = self.table.focus()
        if selected:
            value = self.table.item(selected,"values")
            self.id_var = value[0]
            self.name_var.set(value[1])
            self.category_var.set(value[2])
            self.price_var.set(value[3])
            self.stock_var.set(value[4])

    def _add(self):
        name = self.name_var.get()
        category = self.category_var.get()
        price = self.price_var.get()
        stock = self.stock_var.get()
        success , message = self.controller.add_product(self.user[0],name,category,price,stock)
        if success:
            messagebox.showinfo("Success",message)
            self._load_product()
            self._clear()
        else :
            messagebox.showerror("Error",message)

    def _update(self):
        name = self.name_var.get()
        category = self.category_var.get()
        price = self.price_var.get()
        stock = self.stock_var.get()
        success , message = self.controller.update_product(self.user[0],self.id_var,name,category,price,stock)
        if success:
            messagebox.showinfo("Success",message)
            self._load_product()
            self._clear()
        else:
            messagebox.showerror("Error",message)


    def _delete(self):
        success , message = self.controller.delete_product(self.user[0],self.id_var)
        if success:
            messagebox.showinfo("Success",message)
            self._load_product()
            self._clear()
        else:
            messagebox.showerror("Error",message)



    def _search(self):
            name = self.name_var.get()
            success, products = self.controller.search_product(name)
            if success:

                for row in self.table.get_children():
                    self.table.delete(row)
                for p in products:
                    self.table.insert("", END, values=p)
            else:
                messagebox.showerror("Error", products)




















