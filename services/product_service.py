from exception.exception import InvalidProductDataException
from exception.exception import ProductNotFoundException
from repositories.product_repository import ProductRepository
from services.log_service import LogService
from utils.validators import validate_name , validate_stock , validate_price
class ProductService:
    def __init__(self,conn):
        self.repo = ProductRepository(conn)
        self.log_svs = LogService(conn)

    def add_product(self,user_id,name,category,price,stock):
        if not validate_name(name):
            raise InvalidProductDataException('Product Name should be a valid product name')
        if not validate_price(price):
            raise InvalidProductDataException('Product Price should be positive')
        if not validate_stock(stock):
            raise InvalidProductDataException('Product Stock cannot be negative')
        self.repo.save(name,category,price,stock)
        self.log_svs.log(user_id,'Added Product',f"Product {name} Saved")

    def update_product(self,user_id,id,name,category,price,stock):
        if not validate_name(name):
            raise InvalidProductDataException('Product Name should be a valid product name')
        if not validate_price(price):
            raise InvalidProductDataException('Product Price should be positive')
        if not validate_stock(stock):
            raise InvalidProductDataException('Product Stock cannot be negative')
        self.repo.update(id,name,category,price,stock)
        self.log_svs.log(user_id,'Updated Product',f"Product {name} Saved")

    def delete_product(self, user_id, id):
        product = self.repo.find_by_id(id)
        if not product:
            raise ProductNotFoundException(f'Product {id} not found')
        self.repo.delete(id)
        self.log_svs.log(user_id, 'Deleted Product', f"Product {id} Deleted")

    def search_product(self,name):
        return self.repo.find_by_name(name)


    def get_all_products(self):
        return self.repo.find_all()


