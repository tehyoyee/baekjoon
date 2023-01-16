# 2477.py
# 23.01.17 01:29 ~ 02:20

import sys
input = sys.stdin.readline
from collections import deque

k = int(input())
graph = deque()
order = []
long_side = []
num = [0] * 4
for _ in range(6):
	a, b = map(int, input().split())
	graph.append([a - 1, b])
	num[a - 1] += 1
	order.append(a - 1)
for i in range(4):
	if num[i] == 1:
		long_side.append(i)
while graph[0][0] not in long_side or graph[1][0] not in long_side:
	graph.rotate()
print(k * (graph[0][1] * graph[1][1] - graph[3][1] * graph[4][1]))