class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 10

    def brake(self):
        if self.speed >= 10:
            self.speed -= 10
        else:
            self.speed = 0

    def show_speed(self):
        print("Speed:", self.speed)

car = Car("Toyota")
car.accelerate()
car.show_speed()
car.brake()
car.show_speed()
