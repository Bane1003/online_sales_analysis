from product_manager import ProductManager
from product import Product
from cart import Cart

prom = ProductManager()

p1 = Product("majica", 1500, 15)
p2 = Product("patike", 8500, 12)
p3 = Product("dukserica", 2500, 13)
p4 = Product("trenerka", 3000, 16)
p5 = Product("lopta", 1500, 11)

prom.add_product (p1)
prom.add_product (p2)
prom.add_product (p3)
prom.add_product (p4)
prom.add_product (p5)

prom.show_all_products()
prom.total_sum()

cart = Cart()

cart = Cart()
cart.add_to_cart(p1)
cart.add_to_cart(p3)
cart.add_to_cart(p5)

cart.show_cart()
cart.total_cart_value()
