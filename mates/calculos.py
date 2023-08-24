import math
from typing import Callable


def sumatoria(n: int, f: Callable[[int], float], m: int = 0):
    output = 0
    for i in range(m, n + 1):
        output += f(i)
    return output

def l(k: int):
    return k / math.pow(k + 1, 2)

for i in range(0, 100):
    o = sumatoria(i, l)
    prev = sumatoria(i - 1, l)
    if prev == 0:
        print(f"{i}:", o)
        continue
    print(f"{i}:", o, f"({o / prev}%, {o - prev})")

    if False:
        print(
            "Fórmula general sumatoria:",
        )
