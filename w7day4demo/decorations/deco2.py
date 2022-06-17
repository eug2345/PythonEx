def my_first_decorator(func):
    def wrapper(name):
        print("This is some new functionality!!")
        return func(name)

    return wrapper

def greet(name):
    return f"Hello, {name}!"

greet = my_first_decorator(greet)
print(greet("Bob Smith"))

def wrapper(*args):
   ...