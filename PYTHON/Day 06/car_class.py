class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

car1 = Car("Toyota", "Corolla", "Red")
car2 = Car("Honda", "Civic", "Blue")
car3 = Car("Ford", "Mustang", "Black")

print(car1.brand, car1.model, car1.color)
print(car2.brand, car2.model, car2.color)
print(car3.brand, car3.model, car3.color)
