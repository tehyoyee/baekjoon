# 2869 py

import math

a, b, v = map(int, input().split())

v = (v - b) / (a - b)

print(math.ceil(v))