from exception.exception import AuthenticationException
from services.auth_service import AuthService

class AuthController:
    def __init__(self,conn):
        self.auth_service = AuthService(conn)

    def login(self,username,password):
        try :
            user = self.auth_service.login(username,password)
            return True ,user, "Login Successful"
        except AuthenticationException as e:
            return False,None, str(e)

    def logout(self,user_id):
        try:
            self.auth_service.logout(user_id)
            return True , "Logout Successful"
        except Exception as e:
            return False, str(e)
