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

        print(f"Ukupna vrednost svih proizvoda je: {sum}")
