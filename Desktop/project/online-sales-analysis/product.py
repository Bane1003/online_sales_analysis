class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def product_info(self):
        print(f"Product: {self.name} whose price is: {self.price}, we have {self.quantity} of them.")
         
    def update_value(self, value):
        self.quantity += value