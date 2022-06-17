 # Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

    # <EXAMPLES>

    # five() → [100,102,122,198,200]
    # five() → [108,104,106,188,200]
    # five() → [154,102,132,178,164]

from math import pi, floor
from random import randint

def random_pi():
    return(randint(100, 200) * pi)

for _ in range(5):
    print(random_pi())

