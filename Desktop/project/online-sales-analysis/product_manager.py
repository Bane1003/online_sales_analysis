from product import Product
class ProductManager():
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_all_products(self):
        if self.products !=[]:
            for i in self.products:
                print(i.name)

    def total_sum(self):
        sum = 0
        if self.products != []:
            for i in self.products:
                sum += i.price * i.quantity
        print(f"Sum of all products: {sum}")
<<<<<<< HEAD
=======

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return
>>>>>>> add-product-removal
