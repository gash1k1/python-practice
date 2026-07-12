class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def info(self):
        print(f'{self.brand}, скорость {self.speed} км/ч')

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors
    def car_info(self):
        print(f'{self.brand}, {self.doors} дверей')
    def info(self):
        print(f"Это машина {self.brand}")

if __name__ == '__main__':
    us = Vehicle('жигуль', 12)
    us2 = Car('мазда', 12, 4)
    us2.info()
    us.info()
