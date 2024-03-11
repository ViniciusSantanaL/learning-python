def my_decorator(func):
    def wrapper():
        print("Before calling")
        func()
        print("After calling")
    return wrapper


@my_decorator
def my_function():
    print("My function was called")


# my_function()

class MyDecoratorClass:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> None:
        print("Before calling")
        self.func()
        print("After calling")


@MyDecoratorClass
def simple_function():
    print("My simple function was called")


simple_function()
