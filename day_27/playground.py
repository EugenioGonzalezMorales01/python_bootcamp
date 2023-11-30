def add(*args):
    result = 0
    for n in args:
        result += n
    return result


def calculate(number, **kwargs):
    print(kwargs)
    number += kwargs["add"]
    number *= kwargs["multiply"]
    print(number)

print(add(1, 2, 3, 4, 5))

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")

print(my_car.model)