from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Car(Vehicle):
    def turn_off(self):
        pass

    def __init__(self):
        pass

    def turn_on(self):
        return print('Vrum Vrum')


car = Car()
car.turn_on()
car.turn_off()