class Coffee:
    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe # Dict {ingredient: quantity, ingredient2: quantity....}

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_recipe(self):
        return self.recipe

# Getter method are used instead of accessing variables directly, to imply encapsulation and future extensibility