# 1037py

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
print(max(num) * min(num))