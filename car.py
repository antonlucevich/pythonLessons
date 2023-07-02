class Car():
    def __init__(self, model, year, engine, price, mileage):
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def description_car(self):
        description = self.model + " " + str(self.year) + " " + str(self.engine) + " " + str(self.price) + " " + str(self.mileage) + " " + str(self.wheels)
        print("Новая машина: " + description)

    def update_wheels(self, count_wheels):
        self.wheels = count_wheels

class Truck(Car):
    def __init__(self, model, year, engine, price, mileage):
        super().__init__(model, year, engine, price, mileage)
        self.wheels = 8

some_one_car = Car("Opel", 2000, 3, 800, 250000)
some_one_car.description_car()

some_truck_car = Truck("VW", 1990, 6, 2000, 600000)
some_truck_car.description_car()