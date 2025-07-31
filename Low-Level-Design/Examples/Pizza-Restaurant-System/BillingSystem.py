from Order import Order

class BillingSystem:
    @staticmethod
    def generate_invoice(order: Order):
        print("\n----- Invoice -----")
        for i, pizza in enumerate(order.pizzas):
            print(f"{i+1}. {pizza.name} - ${pizza.calculate_price():.2f}")
        print(f"Total: ${order.calculate_total():.2f}")
        print("-------------------\n")