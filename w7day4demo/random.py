from math import pi, floor
from random import randint

def random_pi():
    return(randint(1, 10) * pi)

for _ in range(5):
    print(random_pi())
