from product_manager import ProductManager
from product import Product


prom = ProductManager()

p1 = Product("kosulja", 1500, 15)
p2 = Product("patike", 8500, 12)
p3 = Product("jakna", 2500, 13)
p4 = Product("trenerka", 3000, 16)
p5 = Product("reket", 1500, 11)

prom.add_product (p1)
prom.add_product (p2)
prom.add_product (p3)
prom.add_product (p4)
prom.add_product (p5)



