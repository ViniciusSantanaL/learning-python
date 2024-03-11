# @classmethod
# @staticmethod

class MyClass:
    value = 10  # attribute of class

    def __init__(self, name):
        self.name = name  # attribute of instance

    def method_instance(self):
        return self.name

    @classmethod
    def method_class(cls):
        return print(f"I am a class, value static: {cls.value}")

    @staticmethod
    def method_static():
        return print("I am a static method")


obj = MyClass("John")
print(obj.method_instance())
MyClass.method_class()

