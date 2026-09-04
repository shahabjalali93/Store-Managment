from exception.exception import AuthenticationException
from repositories.user_repository import UserRepository
from services.log_service import LogService
class AuthService:
    def __init__(self,conn):
        self.repo = UserRepository(conn)
        self.log = LogService(conn)

    def login(self,username,password):
        find_by_username = self.repo.find_by_username(username)
        if not find_by_username or find_by_username[2]!=password:
            raise AuthenticationException('Invalid Username or Password')
        self.log.log(find_by_username[0],'LOGIN',f"{username} Logged In")
        return find_by_username

    def logout(self,user_id):
        self.log.log(user_id ,'LOGGED OUT',f"User {user_id} logged out" )
