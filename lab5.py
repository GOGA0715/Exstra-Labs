class Person:
    def __init__(self, full_name, driving_experience):
        self.full_name = full_name
        self.driving_experience = driving_experience

class Driver(Person):
    def __init__(self, full_name, driving_experience):
        super().__init__(full_name, driving_experience)

class Engine:
    def __init__(self, power, manufacturer):
        self.power = power
        self.manufacturer = manufacturer

class Car:
    def __init__(self, brand, car_class, weight, driver, engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turn_right(self):
        print("Поворот направо")

    def turn_left(self):
        print("Поворот налево")

    def __str__(self):
        return f"Car: {self.brand}, Class: {self.car_class}, Weight: {self.weight}, " \
               f"Driver: {self.driver.full_name}, Engine: {self.engine.power}HP {self.engine.manufacturer}"

class Lorry(Car):
    def __init__(self, brand, car_class, weight, driver, engine, cargo_capacity):
        super().__init__(brand, car_class, weight, driver, engine)
        self.cargo_capacity = cargo_capacity

    def __str__(self):
        return f"{super().__str__()}, Cargo Capacity: {self.cargo_capacity} tons"

class SportCar(Car):
    def __init__(self, brand, car_class, weight, driver, engine, max_speed):
        super().__init__(brand, car_class, weight, driver, engine)
        self.max_speed = max_speed

    def __str__(self):
        return f"{super().__str__()}, Max Speed: {self.max_speed} km/h"

# Пример использования
driver1 = Driver("Иван Иванов", 5)
engine1 = Engine(200, "Toyota")
car1 = Car("Toyota Camry", "Sedan", 1500, driver1, engine1)

driver2 = Driver("Петр Петров", 10)
engine2 = Engine(300, "Ferrari")
sport_car = SportCar("Ferrari 458", "Coupe", 1400, driver2, engine2, 350)

driver3 = Driver("Григорий Григорьев", 8)
engine3 = Engine(400, "Volvo")
lorry = Lorry("Volvo FH16", "Truck", 8000, driver3, engine3, 20)

# Тестирование методов
car1.start()
car1.turn_left()
car1.stop()

print(car1)

sport_car.start()
sport_car.turn_right()
sport_car.stop()

print(sport_car)

lorry.start()
lorry.turn_left()
lorry.stop()

print(lorry)
