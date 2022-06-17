def greet(name, greeting="Hello"):
    return f"{greeting} {name}"

print(greet("Steve"))  # Prints "Hello Steve"
print(greet("Bill", "Hola"))  # Prints "Hola Bill"


def greet(name, greeting="Hello"):
    return f"{greeting} {name}"

print(greet("Ollie", greeting="Hey"))  # Prints "Hey Ollie"