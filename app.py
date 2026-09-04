from repositories.database import get_connection
from repositories.user_repository import UserRepository

conn = get_connection('data/store.db')
repo = UserRepository(conn)
users = repo.find_all()
print(users)