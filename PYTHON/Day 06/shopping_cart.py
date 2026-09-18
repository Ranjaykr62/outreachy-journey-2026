class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for p in self.products:
            print(p.name, p.price)

    def calculate_total(self):
        return sum(p.price for p in self.products)

cart = ShoppingCart()
p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)

cart.add_product(p1)
cart.add_product(p2)

cart.show_products()
print("Total:", cart.calculate_total())
