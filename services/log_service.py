from datetime import datetime
from repositories.log_repository import LogRepository
class LogService:
    def __init__(self,conn):
        self.conn = conn
        self.repo = LogRepository(self.conn)

    def log (self,user_id,action,description):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.repo.save(user_id,action,description,timestamp)
    def get_all_logs(self):
        return self.repo.find_all()
