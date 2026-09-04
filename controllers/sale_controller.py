from services.sale_service import SalesService

class SalesController :
    def __init__(self,conn):
        self.sale_service = SalesService(conn)

    def register_sale(self,user_id,customer_id,product_id,quantity):
        try :
            total =self.sale_service.register_sale(user_id,customer_id,product_id,quantity)
            return True, f"Sale {total} has been registered"
        except ValueError as e:
            return False, str(e)



    def get_all_sales(self):
        try :
            return True , self.sale_service.get_all_sales()
        except Exception as e:
            return False, str(e)


