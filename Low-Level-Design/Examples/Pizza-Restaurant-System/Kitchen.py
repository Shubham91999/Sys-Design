from Order import Order
from Order import OrderStatus

class Kitchen:
    def __init__(self):
        self.pending_orders = []

    def receive_order(self, order: Order):
        print(f"Received Order for {order.customer_name}")
        self.pending_orders.append(order)

    def prepare_order(self, order: Order):
        order.update_status(OrderStatus.PREPARING)
        print('Preparing Order..')

        order.update_status(OrderStatus.READY)
        print("Order Ready")