from product_manager import ProductManager
from product import Product

proman = ProductManager()

proman.add_product(Product("majica", 1500, 15))
proman.add_product(Product("patike", 8500, 12))
proman.add_product(Product("dukserica", 2500, 13))
proman.add_product(Product("trenerka", 3000, 12))
proman.add_product(Product("lopta", 1500, 10))

print(proman.total_sum())
print(proman.show_all_products())