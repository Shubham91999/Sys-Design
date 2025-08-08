from enum import Enum
import uuid
from datetime import datetime
from abc import ABC, abstractmethod

class PizzaSize(Enum):
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'LARGE'
    EXTRA_LARGE = 'Extra Large'

class CrustType(Enum):
    THIN = 'Thin'
    THICK = 'Thick'
    CHEESE_BURST = 'Cheese Burst'

class Topping:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Pizza:
    def __init__(self, name: str, size: PizzaSize, crust: CrustType, base_price: float):
        self.name = name
        self.size = size
        self.crust = crust
        self.base_price = base_price
        self.toppings = []

    def add_topping(self, topping: Topping):
        if topping not in self.toppings:
            self.toppings.append(topping)

    def calculate_price(self):
        return self.base_price + sum(t.price for t in self.toppings)
    
class Menu:
    def __init__(self):
        self.available_pizzas = []
    
    def add_pizza(self, pizza: Pizza):
        self.available_pizzas.append(pizza)

    def show_menu(self):
        for i, pizza in enumerate(self.available_pizzas):
            print(f"{i+1}. {pizza.name} ({pizza.size.value} - ${pizza.calculate_price():.2f})")
        
class OrderStatus(Enum):
    RECEIVED = 'Order received'
    PREPARING = 'Your order is getting prepared'
    READY = 'Your order is ready'
    DELIVERED = 'Your pizza is delivered'

class Order:
    def __init__(self, customer_name: str):
        self.id = uuid.uuid4()
        self.customer_name= customer_name
        self.pizzas = []
        self.status = OrderStatus.RECEIVED
        self.timestamp = datetime.now()

    def add_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)

    def display_order(self):
        for i, pizza in enumerate(self.pizzas):
            print(f"{i+1}. {pizza.name} ({pizza.size.value} - ${pizza.calculate_price():.2f})")

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        return self.status.value
    
    def calculate_total(self):
        return sum(pizza.calculate_price() for pizza in self.pizzas)
    
class Kitchen:
    def __init__(self):
        self.pending_orders = []

    def recieve_order(self, order: Order):
        print(f"Order received for {order.customer_name}")
        self.pending_orders.append(order)

    def prepare_order(self, order: Order):
        #order.update_status(OrderStatus.PREPARING)
        print(order.update_status(OrderStatus.PREPARING))

class BillingSystem(ABC):
    @staticmethod
    def generate_invoice(order: Order):
        print("\n----- Invoice -----")
        for i, pizza in enumerate(order.pizzas):
            print(f"{i+1}. {pizza.name} - ${pizza.calculate_price():.2f}")
        print(f"Total: ${order.calculate_total():.2f}")
        print("-------------------\n")

    @abstractmethod
    def payment():
        pass

class CreditCardPayment(BillingSystem):
    def payment(self, order: Order):
        price = order.calculate_total()
        print(f"Payment of ${price:.2f} completed using Credit Card")

class PaypalPayment(BillingSystem):
    def payment(self, order: Order):
        price = order.calculate_total()
        print(f"Payment of ${price:.2f} completed using Paypal")

class StripePayment(BillingSystem):
    def payment(self, order: Order):
        price = order.calculate_total()
        print(f"Payment of ${price:.2f} completed using Stripe")


# Create pizza with toppings
pizza1 = Pizza("Veggie Delight", PizzaSize.LARGE, CrustType.CHEESE_BURST, base_price=10.0)
pizza1.add_topping(Topping("Mushrooms", 1.0))
pizza1.add_topping(Topping("Olives", 1.2))
pizza1.add_topping(Topping("Jalapenos", 1.5))

# Create another pizza
pizza2 = Pizza("Pepperoni", PizzaSize.MEDIUM, CrustType.THICK, base_price=9.0)
pizza2.add_topping(Topping("Extra Cheese", 1.8))

# Create an order
order = Order("Shubham")
order.add_pizza(pizza1)
order.add_pizza(pizza2)

# Process through kitchen
kitchen = Kitchen()
kitchen.recieve_order(order)
kitchen.prepare_order(order)

# Generate invoice
BillingSystem.generate_invoice(order)

# Pay using chosen method
payment_method = StripePayment()
payment_method.payment(order)
