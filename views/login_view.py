from tkinter import *
from tkinter import messagebox
from controllers.auth_controller import AuthController

class LoginView :
    def __init__(self,conn):
        self.conn = conn
        self.auth_controller = AuthController(conn)
        self.win =Tk()
        self.win.geometry("300x150")
        self.win.title("Login")
        self._build_ui()
        self.win.mainloop()

    def _build_ui(self):
        Label(self.win, text="Username").grid(row=0, column=0)
        self.username_var = StringVar()
        Entry(self.win, textvariable = self.username_var).grid(row=0, column=1)
        Label(self.win, text="Password").grid(row=1, column=0)
        self.password_var = StringVar()
        Entry(self.win, textvariable =self.password_var, show = "*").grid(row=1, column=1)
        Button(self.win ,text = "Login",command = self._on_login).grid(row=2, column=1)

    def _on_login(self):
        username = self.username_var.get()
        password = self.password_var.get()
        success , user ,message =self.auth_controller.login(username,password)
        if success:
            self.win.destroy()
            from views.main_view import MainView
            MainView(self.conn,user)

        else :
            messagebox.showerror("Error","Login Failed")







