from tkinter import *
from tkinter import ttk
from controllers.log_controller import LogController
class LogView :
    def __init__(self,parent,conn):
        self.parent = parent
        self.controller = LogController(conn)
        self._build_ui()
        self._load()

    def _build_ui(self):
        self.table = ttk.Treeview(self.parent, columns=("id","user_id", "action", "description","timestamp"),show ="headings")
        self.table.heading("id",text="ID")
        self.table.heading("user_id",text= "User ID")
        self.table.heading("action",text= "Action")
        self.table.heading("description", text="Description")
        self.table.heading("timestamp",text= "Timestamp")
        self.table.pack(fill=BOTH, expand = True, padx=10, pady=10)

    def _load(self):
        for row in  self.table.get_children():
            self.table.delete(row)
        success, logs = self.controller.get_all_logs()
        if success:
            for log in logs:
                self.table.insert('', 'end', values=log)




