from exception.exception import InvalidCustomerDataException, CustomerNotFoundException
from services.customer_service import CustomerService

class CustomerController:
    def __init__(self,conn):
        self.service = CustomerService(conn)

    def add_customer(self,user_id,name,phone_number):
        try:
            self.service.add_customer(user_id,name,phone_number)
            return True ,"New customer has been added"
        except InvalidCustomerDataException as e:
            return False, str(e)

    def update_customer(self,user_id,id,name,phone_number):
        try:
            self.service.update_customer(user_id,id,name,phone_number)
            return True ,"Customer has been updated"
        except InvalidCustomerDataException as e:
            return False, str(e)

    def delete_customer(self,user_id,id):
        try:
             self.service.delete_customer(id, user_id)
             return True ,"Customer has been deleted"
        except CustomerNotFoundException as e:
            return False, str(e)

    def get_all_customers(self):
        try:
            return True, self.service.get_all_customers()
        except Exception as e:
            return False, str(e)

    def search_customer(self,name):
        try:
            return True , self.service.search_customer(name)
        except Exception as e:
            return False, str(e)


