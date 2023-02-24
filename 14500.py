# 14500.py
# 23.02.24. 10:05 ~ 11:25

import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def dfs(i, j, v, l):
	result = 0
	visit[i][j] = 1
	v += graph[i][j]
	if l == 4:
		return v
	else:
		for k in range(4):
			ni, nj = i + di[k], j + dj[k]
			if graph[ni][nj] and not visit[ni][nj]:
				visit[ni][nj] = 1
				result = max(result, dfs(ni, nj, v, l + 1))
				visit[ni][nj] = 0
	visit[i][j] = 0
	return result

def bfs(i, j):
	total = graph[i][j]
	tmp = 1000
	flag = 0
	for k in range(4):
		if graph[i + di[k]][j + dj[k]]:
			tmp = min(tmp, graph[i + di[k]][j + dj[k]])
			total += graph[i + di[k]][j + dj[k]]
			flag += 1
	if flag == 3:
		return total
	elif flag == 4:
		return total - tmp
	return 0

result = 0
n, m = map(int, input().split())
graph = []
visit = [[0] * (m + 2) for _ in range(n + 2)]
graph.append([0] * (m + 2))
for _ in range(n):
	graph.append([0] + list(map(int, input().split())) + [0])
graph.append([0] * (m + 2))

for i in range(1, n + 1):
	for j in range(1, m + 1):
		if i % 3 == 1 and j % 3 == 1:
			result = max(result, dfs(i, j, 0, 1))
		result = max(result, bfs(i, j))
print(result)