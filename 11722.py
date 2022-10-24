# 11722.py

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
check = [0] * n
for i in range(n):
	for j in range(i):
		if arr[j] > arr[i] and check[j] >= check[i]:
			check[i] = check[j] + 1
	if check[i] == 0:
		check[i] = 1
print(max(check))
