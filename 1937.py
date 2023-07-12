# 1937.py
# 23.04.27. 08:13 ~ x

import sys
input = sys.stdin.readline

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

N = int(input())
graph = []
for _ in range(N):
	graph.append(list(map(int, input().split())))
visit = [[0] * N for _ in range(N)]
result = 0

def dfs(ci, cj):
	if visit[ci][cj]:
		return visit[ci][cj]
	visit[ci][cj] = 1
	for k in range(4):
		ni, nj = ci + di[k], cj + dj[k]
		if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] > graph[ci][cj]:
			visit[ci][cj] = max(dfs(ni, nj) + 1, visit[ci][cj])
	return visit[ci][cj]

for i in range(N):
	for j in range(N):
		result = max(dfs(i, j), result)

print(result)