# 1012.py

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, graph):
	graph[y][x] = 0
	for i in range(4):
		if 0 <= y + dy[i] <= n - 1 and 0 <= x + dx[i] <= m - 1:
			if graph[y + dy[i]][x + dx[i]] == 1:
				dfs(x + dx[i], y + dy[i], graph)

t = int(input())
for _ in range(t):
	m, n, k = map(int, input().split())
	graph = [[0] * m for _ in range(n)]
	for _ in range(k):
		x, y = map(int, input().split())
		graph[y][x] = 1
	result = 0
	for i in range(n):
		for j in range(m):
			if graph[i][j] == 1:
				dfs(j, i, graph)
				result += 1
	print(result)