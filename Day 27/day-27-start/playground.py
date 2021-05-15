def add(*args):
    print(args[0])  # can get the element like a list
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 2, 3, 4, 5))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        # Using .get() so that it just return None instead of error if the specific argument not specified when call
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.make)