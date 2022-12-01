# 1931.py

import sys
input = sys.stdin.readline

n = int(input())
arr = [[0, 0]]
result = 0
for _ in range(n):
	arr.append(list(map(int, input().split())))
arr.sort(key = lambda x : x[0])
arr.sort(key = lambda x : x[1])
pivot = 0
for i in range(1, len(arr)):
	if arr[pivot][1] <= arr[i][0]:
		pivot = i
		result += 1
print(arr)
print(result)