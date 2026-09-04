import re
def validate_name (name: str) -> bool:
    return bool(re.match(r"^[a-zA-Z]{3,50}$", name))
def validate_phone (phone: str) -> bool:
    return bool(re.match(r"^[0-9]{10,11}$", phone))
def validate_price (price)-> bool:
    return isinstance(price,(int,float)) and price > 0
def validate_stock (stock)-> bool:
    return isinstance(stock,int) and stock >= 0
def validate_quantity (quantity)-> bool:
    return isinstance(quantity,int) and quantity >= 1
