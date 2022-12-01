# 16724.py

import sys
input = sys.stdin.readline

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]
dire = ['D', 'U', 'L', 'R']

def union(a, b):
	a, b = find(a), find(b)
	union[max(a, b)] = min(a, b)

def find(x):
	if graph[x] == x:
		return x
	graph[x] = find(graph[x])
	return graph[x]

n, m = map(int, input().split())
parent = [[1] * m for _ in range(n)]
for i in range(n * m):
	parent[i // m][i % m] += i
graph = []
for _ in range(n):
	graph.append(input())
for i in range(n):
	for j in range(m):
		if parent[i][j] != i * n + j:
			continue
		q = [[i, j]]
		while q:
			cur_i, cur_j = q.pop(0)
			for k in range(4):
				if graph[cur_i][cur_j] == dire[k]:
					q.append(graph[cur_i][cur_j])
