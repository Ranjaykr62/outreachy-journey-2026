class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

mobile1 = Mobile("Samsung", "Galaxy S21", 60000)
mobile2 = Mobile("Apple", "iPhone 13", 80000)

print(mobile1.brand, mobile1.model, mobile1.price)
print(mobile2.brand, mobile2.model, mobile2.price)
