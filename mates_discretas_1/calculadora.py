import math
import fractions
from fractions import Fraction as Fr
from pprint import pprint
from math import pow
from pprint import pprint
from typing import Callable, List


def sumatoria(n: int, f: Callable[[int], float], m: int = 0):
    output = 0
    for i in range(m, n + 1):
        output += f(i)
    return output

for i in range(1, 100):
    iter = sum(1 for k in range(100, 1000) if k % i == 0)
    const = math.floor(len(range(100, 1000)) / i)
    if iter != const:
        pprint((i, iter, const, len(range(100, 1000)) / i))
        pass
