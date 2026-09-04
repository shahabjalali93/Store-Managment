class Product:
    def __init__(self, product_id, name ,category,price, stock):
        self.id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def __repr__(self):
        return f"<Product id={self.id} name={self.name} category={self.category} price={self.price}  stock={self.stock}>"

    def to_tuple(self):
        return self.id, self.name,self.category, self.price, self.stock
