from datetime import datetime
from enum import Enum
from Pizza import Pizza

class OrderStatus(Enum):
    PENDING = 'Pending'
    PREPARING = 'Preparing'
    READY = 'Ready'
    DELVERED = 'Delivered'

class Order:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.pizzas = []
        self.status = OrderStatus.PENDING
        self.timestamp = datetime.now()

    def add_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)

    def calculate_total(self):
        return sum(pizza.calculate_price() for pizza in self.pizzas)
    
    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        