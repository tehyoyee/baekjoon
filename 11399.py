# 11399 py

import sys
input = sys.stdin.readline

result = 0
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(n):
    result += sum(arr[0:i + 1])
print(result)