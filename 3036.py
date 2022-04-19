# 3036py

import sys
import math

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
for i in range(n - 1):
    print("%s%c%s" %(arr[0] // math.gcd(arr[0], arr[i + 1]), '/', arr[i + 1] // math.gcd(arr[0], arr[i + 1])))
