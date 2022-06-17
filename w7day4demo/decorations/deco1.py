def case(func, string):
    return func(string)

print(case(str.upper, "hello world")) # Prints HELLO WORLD
print(case(str.lower, "LOREM IPSUM")) # Prints lorem ipsum