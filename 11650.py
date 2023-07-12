# 11650.py
# 23.07.08 01:08 ~

import sys
input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
	graph.append(list(map(int, input().split())))

graph.sort(key=lambda x:(x[0], x[1]))
for x in graph:
	print(*x)