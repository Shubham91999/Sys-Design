from PizzaSize import PizzaSize
from CrustType import CrustType
from Topping import Topping


class Pizza:
    def __init__(self, name: str, size: PizzaSize, crust: CrustType, base_price: float):
        self.name = name
        self.size = size
        self.crust = crust
        self.base_price = base_price
        self.toppings = []

    def add_topping(self, topping: Topping):
        self.toppings.append(topping)

    def calculate_price(self):
        return self.base_price + sum(t.price for t in self.toppings)