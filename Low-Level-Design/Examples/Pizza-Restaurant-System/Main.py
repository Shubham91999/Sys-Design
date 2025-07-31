from Topping import Topping
from Pizza import Pizza
from PizzaSize import PizzaSize
from CrustType import CrustType
from Order import Order
from Kitchen import Kitchen
from Menu import Menu
from BillingSystem import BillingSystem

if __name__=="__main__":

    # Create Toppings
    cheese = Topping("Extra Cheese", 1.5)
    mushrooms = Topping("Mushrooms", 1.0)

    # Create pizzas
    margherita = Pizza("Margherita", PizzaSize.MEDIUM, CrustType.THIN, 8.0)
    margherita.add_topping(cheese)

    pepperoni = Pizza("Pepperoni", PizzaSize.LARGE, CrustType.CHEESE_BURST, 10.0)
    pepperoni.add_topping(mushrooms)

    # Create menu
    menu = Menu()
    menu.add_pizza(margherita)
    menu.add_pizza(pepperoni)
    menu.show_menu()

    # Customer places an order
    order = Order("Alice")
    order.add_pizza(margherita)
    order.add_pizza(pepperoni)

    # Kitchen processes order
    kitchen = Kitchen()
    kitchen.receive_order(order)
    kitchen.prepare_order(order)


    print("\n[DEBUG] Order Contents:")
    for idx, pizza in enumerate(order.pizzas):
        print(f"  Pizza {idx+1}: {pizza.name}, Type: {type(pizza)}")

    # Billing
    BillingSystem.generate_invoice(order)