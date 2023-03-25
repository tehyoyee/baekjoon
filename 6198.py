# 6198.py
# 23.03.14. 15:24 ~ 15:51

import sys
input = sys.stdin.readline
from collections import deque

result = 0
N = int(input())
graph = []
buildings = deque([])
buildings.append(int(input()))
for i in range(1, N):
	tmp = int(input())
	while buildings[-1] <= tmp:
		buildings.pop()
		if len(buildings) == 0:
			break
	result += len(buildings)
	buildings.append(tmp)

print(result)