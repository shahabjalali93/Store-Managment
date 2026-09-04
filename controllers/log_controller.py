from services.log_service import LogService
class LogController:
    def __init__(self,conn):
        self.service = LogService(conn)

    def get_all_logs(self):
        try :
            return True , self.service.get_all_logs()
        except Exception as e :
            return False, str(e)


