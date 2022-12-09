import numpy as np
from typing import Union


def power(x: float, y: int) -> float:
    result = 1.0
    while True:
        t = y % 2
        y = int(np.floor(y / 2))
        if t == 1:
            result = result * x
        if y == 0:
            break
        x = x * x
    return result


print(f"power(2,10) = {power(2, 10)}")
print(f"power(2.0,10) = {power(2.0, 10)}")
