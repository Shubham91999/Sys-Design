import threading
class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self._lock = threading.Lock()

    def get_name(self):
        return self.name
    
    def get_quantity(self):
        with self._lock:
            return self.quantity
    
    def update_quantity(self, amount):
        with self._lock:
            self.quantity += amount

# Threading lock added around the get_quantity() and update_quantity() methods. This ensures atomicity - two threads won't read/update at the same time.

    