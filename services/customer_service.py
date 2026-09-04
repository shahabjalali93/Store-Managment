from utils.validators import validate_name ,  validate_phone
from exception.exception import InvalidCustomerDataException, CustomerNotFoundException
from repositories.customer_repository import CustomerRepository
from services.log_service import LogService
class CustomerService:
    def __init__(self,conn):
        self.repo = CustomerRepository(conn)
        self.log_svc = LogService(conn)

    def add_customer(self,user_id,name,phone_number ):
        if not validate_name(name):
            raise InvalidCustomerDataException('Invalid customer name')
        if not validate_phone(phone_number):
            raise InvalidCustomerDataException('Invalid phone number')
        self.repo.save(name, phone_number)
        self.log_svc.log(user_id,'Added new customer',f'Customer {name} {phone_number} has been added')


    def update_customer(self,id,user_id,name,phone_number):
        if not validate_name(name):
            raise InvalidCustomerDataException('Invalid customer name')
        if not validate_phone(phone_number):
            raise InvalidCustomerDataException('Invalid phone number')
        self.repo.update(id, name, phone_number)
        self.log_svc.log(user_id,'Updated customer',f'Customer {name} {phone_number} has been updated')

    def delete_customer(self,id,user_id):
        product = self.repo.find_by_id(id)
        if not product:
            raise CustomerNotFoundException(f'Customer {id} not found')
        self.repo.delete(id)
        self.log_svc.log(user_id,'Deleted customer',f'Customer {id} has been deleted')

    def get_all_customers(self):
        return self.repo.find_all()

    def search_customer(self,name ):
        return self.repo.find_by_name(name)



