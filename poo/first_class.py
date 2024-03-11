class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def talk(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years ")

person = Person("John", 30)
print(person)
print(person.name)
print(person.age)

person.talk()

secondPerson = Person(name="Vinicius", age=32)
