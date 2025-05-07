from Coffee import Coffee
from Ingredient import Ingredient

class CoffeeMachine:
    _instance = None

    def __init__(self):
        if CoffeeMachine._instance is not None:
            raise Exception("This class is Singleton.")
        else:
            CoffeeMachine._instance = self
            self.coffee_menu = []
            self.ingredients = {}
            self._initialize_ingredients()  # calling helper methods to load ingradients and coffee types
            self._initialize_coffee_menu()

    @staticmethod
    def get_instance(): # Ensures only one instance of CoffeeMachine is ever created
        if CoffeeMachine._instance is None:
            CoffeeMachine()
        return CoffeeMachine._instance
    
    def _initialize_coffee_menu(self): # Recipe in dictionary -> new Coffee object -> Appending in coffee_menu list
        espresso_recipe = {
            self.ingredients["Coffee"]:1,
            self.ingredients["Water"]:1
        }
        self.coffee_menu.append(Coffee("Espresso", 2.5, espresso_recipe))

        cappucino_recipe = {
            self.ingredients["Coffee"]: 1,
            self.ingredients["Water"]: 1,
            self.ingredients["Milk"]: 1
        }
        self.coffee_menu.append(Coffee("Cappuccino", 3.5, cappucino_recipe))

        latte_recipe = {
            self.ingredients["Coffee"]: 1,
            self.ingredients["Water"]: 1,
            self.ingredients["Milk"]: 2
        }
        self.coffee_menu.append(Coffee("latte", 4.0, latte_recipe))

    def _initialize_ingredients(self):  # New Ingredient object -> ingredients dict: Ingredient name (key): Ingredient Object
        self.ingredients["Coffee"] = Ingredient("Coffee", 10)
        self.ingredients["Water"] = Ingredient("Water", 10)
        self.ingredients["Milk"] = Ingredient("Milk", 10)

    def display_coffee(self):  # Prints all available coffee drinks and their prices
        print("coffee Menu:")
        for coffee in self.coffee_menu:
            print(f"{coffee.get_name()} - ${coffee.get_price()}")

    def select_coffee(self, coffee_menu): # Takes input from user -> matches with available drinks -> if found returns coffee object or None
        for coffee in self.coffee_menu:
            if coffee.get_name().lower() == coffee_menu.lower():
                return coffee
        return None
    
    def dispense_coffee(self, coffee, payment): # Check payment -> check ingrdients -> update ingredients -> calculate change -> dispence coffee & change
        if payment.get_amount() == coffee.get_price():
            if self._has_enough_ingredients(coffee):
                self._update_ingredients(coffee)
                print(f"Dispencing {coffee.get_name()}...")
                change = payment.get_amount() - coffee.get_price()
                if change > 0:
                    print(f"Please collect your change: ${change}")
            else:
                print(f"Insufficient ingredients to make {coffee.get_name()}")
        else:
            print(f"Insufficient payment for {coffee.get_name()}")

    def _has_enough_ingredients(self, coffee): # Iterate through all ingredients in recipe -> get current quantity for that ingredient -> compare with required quantity
        for ingredient, required_quantity in coffee.get_recipe().items(): 
            if ingredient.get_quantity() < required_quantity:
                return False
            return True
        
    def _update_ingredients(self, coffee):
        for ingredient, required_quantity in coffee.get_recipe().items():
            ingredient.update_quantity(-required_quantity)
            if ingredient.get_quantity() < 3:
                print(f"Low Inventory Alert: {ingredient.get_name()}")

# This is a core controller of the vending machine. It handles initlialization, user interactions, ingredient tracking, and safe resource usauage 
# through shared ingredient objects. We have used Singleton pattern for centralized access and ensured each operation follows single responsibility
# and encapsulation principles. 
        




 
    


