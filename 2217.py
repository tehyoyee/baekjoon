# 2217.py

import sys
input = sys.stdin.readline

n = int(input())
rope = []
result = 0
for _ in range(n):
	rope.append(int(input()))
rope.sort()
for i in range(n):
	result = max(result, (n - i) * rope[i])
print(result)