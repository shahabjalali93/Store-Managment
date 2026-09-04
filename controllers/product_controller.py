from exception.exception import InvalidProductDataException, ProductNotFoundException
from services.product_service import ProductService
class ProductController:
    def __init__(self,conn):
        self.service = ProductService(conn)

    def add_product(self,user_id,name,category,price,stock):
        try :
            self.service.add_product(user_id,name,category,price,stock)
            return True, "Product Added Successfully"
        except InvalidProductDataException as e:
            return False, str(e)

    def update_product(self,user_id,product_id,name,category,price,stock):
        try :
            self.service.update_product(user_id,product_id,name,category,price,stock)
            return True, "Product Updated Successfully"
        except InvalidProductDataException as e:
            return False, str(e)

    def delete_product(self,user_id,product_id):
        try :
            self.service.delete_product(user_id,product_id)
            return True, "Product Deleted Successfully"
        except Exception as e:
            return False, str(e)

    def get_all_products(self):
        try:
             return True, self.service.get_all_products()

        except Exception as e:
            return False, str(e)

    def search_product(self,name):
        try:
            return True, self.service.search_product(name)

        except ProductNotFoundException as e:
            return False, str(e)
