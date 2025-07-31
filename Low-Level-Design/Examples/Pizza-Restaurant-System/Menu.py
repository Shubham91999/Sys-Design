from Pizza import Pizza

class Menu:
    def __init__(self):
        self.available_pizzas = []

    def add_pizza(self, pizza: Pizza):
        self.available_pizzas.append(pizza)

    def show_menu(self):
        for i, pizza in enumerate(self.available_pizzas):
            print(f'{i+1}. {pizza.name} ({pizza.size.value} - ${pizza.calculate_price():.2f})')