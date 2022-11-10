# 10026.py

# 10026 적록색약

# dfs 로 구현.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

n = int(input())
graph = []
visit = [[0] * n for _ in range(n)]

def dfs(i, j, color):
	visit[i][j] = 1
	for k in range(4):
		if 0 <= i + di[k] < n and 0 <= j + dj[k] < n:
			if visit[i + di[k]][j + dj[k]] == 0 and graph[i + di[k]][j + dj[k]] in color:
				dfs(i + di[k], j + dj[k], color)

for _ in range(n):
	graph.append(list(input().rstrip()))

result_1 = 0
for i in range(n):
	for j in range(n):
		color = [graph[i][j]]
		if visit[i][j] == 0:
			result_1 += 1
			dfs(i, j, color)

result_2 = 0
for i in range(n):
	for j in range(n):
		visit[i][j] = 0

for i in range(n):
	for j in range(n):
		color = [graph[i][j]]
		if color[0] == 'R':
			color.append('G')
		elif color[0] == 'G':
			color.append('R')
		if visit[i][j] == 0:
			result_2 += 1
			dfs(i, j, color)
print(result_1, result_2)