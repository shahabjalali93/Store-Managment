from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controllers.customer_controller import CustomerController
class CustomerView :
    def __init__(self,parent,conn,user):
        self._parent = parent
        self._conn = conn
        self.user = user
        self.controller = CustomerController(conn)
        self._build_ui()
        self._load()

    def _build_ui(self):
        form_frame = Frame(self._parent)
        form_frame.pack(fill=X, padx=10, pady=10)
        form_frame.columnconfigure(1, weight=1)

        Label(form_frame, text="Customer Name").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.name_var = StringVar()
        Entry(form_frame, textvariable=self.name_var,bg='white',fg='black', width=30).grid(row=0, column=1, sticky='ew', padx=5, pady=5)

        Label(form_frame, text="Phone Number").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.phone_var = StringVar()
        Entry(form_frame, textvariable=self.phone_var,bg='white',fg='black', width=30).grid(row=1, column=1, sticky='ew', padx=5, pady=5)

        btn_frame = Frame(self._parent)
        btn_frame.pack(fill=X, padx=10, pady=5)
        Button(btn_frame, text="Add", command=self._add_customer).pack(side=LEFT, padx=3)
        Button(btn_frame, text="Update", command=self._update_customer).pack(side=LEFT, padx=3)
        Button(btn_frame, text="Delete", command=self._delete_customer).pack(side=LEFT, padx=3)
        Button(btn_frame, text="Search", command=self._search).pack(side=LEFT, padx=3)
        Button(btn_frame, text="Clear", command=self._clear).pack(side=LEFT, padx=3)

        self.table = ttk.Treeview(self._parent,
            columns=("id","name","phone number"), show="headings")
        self.table.heading("id", text="Customer ID")
        self.table.heading("name", text="Customer Name")
        self.table.heading("phone number", text="Phone Number")
        self.table.pack(fill=BOTH, expand=True, padx=10, pady=10)
        self.table.bind("<<TreeviewSelect>>", self._select)
    def _load(self):
        for row in self.table.get_children():
            self.table.delete(row)
        success , customer = self.controller.get_all_customers()
        if success:
            for c in customer:
                self.table.insert("",END,values=c)

    def _clear(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.id_var = None



    def _select(self,event):
        selected = self.table.focus()
        if selected:
            value = self.table.item(selected,"values")
            self.id_var = int(value[0])
            self.name_var.set(value[1])
            self.phone_var.set(value[2])


    def _add_customer(self):
        name = self.name_var.get()
        phone_number = self.phone_var.get()
        success, message = self.controller.add_customer(self.user[0],name,phone_number)
        if success:
            self._load()
            self._clear()
            messagebox.showinfo("Success",message)
        else:
            messagebox.showerror("Error",message)


    def _update_customer(self):
        name = self.name_var.get()
        phone_number = self.phone_var.get()
        if not hasattr(self, "id_var")or self.id_var is None:
            messagebox.showinfo("Error","Please select a customer.")
            return
        success, message = self.controller.update_customer(self.user[0],self.id_var,name,phone_number)
        if success:
            self._load()
            self._clear()
            messagebox.showinfo("Success",message)
        else:
            messagebox.showerror("Error",message)


    def _delete_customer(self):
        if not hasattr(self, "id_var") or self.id_var is None:
            messagebox.showinfo("Error","Please select a customer.")
            return
        success, message = self.controller.delete_customer(self.id_var,self.user[0])
        if success:
            self._load()
            self._clear()
            messagebox.showinfo("Success",message)
        else:
            messagebox.showerror("Error",message)


    def _search(self):
        name = self.name_var.get()
        success ,customer = self.controller.search_customer(name)
        if success:
            for row in self.table.get_children():
                self.table.delete(row)

            for c in customer:
                self.table.insert("",END,values=c)

        else:
            messagebox.showerror("Error",customer)



