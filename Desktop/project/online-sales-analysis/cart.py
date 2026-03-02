from product import Product
class Cart:
    def __init__(self):
        self.cart_items = []
    
    def add_to_cart(self, product):
        self.cart_items.append(product)
    
    def total_cart_value(self):
        sum = 0
        if self.cart_items != []:
            for i in self.cart_items:
                sum += i.price * i.quantity
        print(f"Sum of cart: {sum}")

    def show_cart(self):
        if self.cart_items !=[]:
            for i in self.cart_items:
                print(i.name)
