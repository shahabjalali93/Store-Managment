from repositories.database import get_connection, create_tables
from views.login_view import LoginView

def main():
    conn = get_connection('data/store.db')
    create_tables(conn)
    LoginView(conn)

if __name__ == '__main__':
    main()