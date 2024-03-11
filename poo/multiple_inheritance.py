class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Mammal(Animal):
    def breastfeed(self):
        return f"{self.name} is breastfeeding."


class Bird(Animal):
    def fly(self):
        print(f"I am flying {self.name}")


class Bat(Mammal, Bird):
    def speak(self):
        return "Pi pi pi"


bat = Bat("Batman")
bat.fly()
bat.speak()
bat.breastfeed()
