# 1932py

import sys

input = sys.stdin.readline

t = int(input())
graph = []
cost = []

for i in range(t):
	graph.append(list(map(int, input().split())))

for i in range(1, t):
	for j in range(i + 1):
		if j == 0:
			graph[i][0] += graph[i - 1][0]
		elif j == i:
			graph[i][j] += graph[i - 1][j - 1]
		else:
			graph[i][j] += max(graph[i - 1][j - 1], graph[i - 1][j])

print(max(graph[t - 1]))