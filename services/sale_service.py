from exception.exception import ProductNotFoundException, InsufficientStockException
from repositories.sale_repository import SalesRepository
from repositories.product_repository import ProductRepository
from services.log_service import LogService
from datetime import datetime

class SalesService:
    def __init__(self,conn):
        self.repo = SalesRepository(conn)
        self.product_repo = ProductRepository(conn)
        self.log_svc = LogService(conn)

    def register_sale(self,user_id,customer_id,product_id,quantity):
        product = self.product_repo.find_by_id(product_id)
        if not product:
            raise ProductNotFoundException ('Product not found')
        if product[4] < quantity :
            raise InsufficientStockException ('Insufficient stock')
        total = product[3] * quantity
        date = datetime.today().strftime('%Y-%m-%d')
        self.repo.save(user_id,customer_id,product_id,quantity,total,date)
        self.product_repo.update_stock(product_id,quantity)
        self.log_svc.log(user_id,'SALE',f"Product {product[1]} X {quantity} Sold ")
        return total

    def get_all_sales(self):
        return self.repo.find_all()



