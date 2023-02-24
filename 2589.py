# 2589.py
# 23.02.24. 09:24 ~ 09:54

from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n, m = map(int, input().split())
graph = []

def bfs(i, j, n, m):
	visit = [[0] * m for _ in range(n)]
	q = deque([[i, j]])
	visit[i][j] = 1
	while q:
		ci, cj = q.popleft()
		for k in range(4):
			ni, nj = ci + di[k], cj + dj[k]
			if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 'L' and not visit[ni][nj]:
				visit[ni][nj] = visit[ci][cj] + 1
				q.append([ni, nj])
	return visit[ci][cj] - 1

result = 0
for _ in range(n):
	graph.append(list(input()))
for i in range(n):
	for j in range(m):
		flag = 0
		for k in range(4):
			ni, nj = i + di[k], j + dj[k]
			if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 'L':
				flag += 1
		if flag <= 2 and graph[i][j] == 'L':
			result = max(result, bfs(i, j, n, m))
print(result)