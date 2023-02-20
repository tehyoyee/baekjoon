# 7569.py
# 23.02.20. 10:48 ~ 10:56

from collections import deque

di = [1, -1, 0, 0, 0, 0]
dj = [0, 0, 1, -1, 0, 0]
dk = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split())
graph = []
result = 0
q = deque()
visit = [[[0] * m for _ in range(n)] for _ in range(h)]

for k in range(h):
	temp = []
	for i in range(n):
		temp.append(list(map(int, input().split())))
		for j in range(m):
			if temp[i][j] == 1:
				q.append([k, i, j])
				visit[k][i][j] = 1
	graph.append(temp)

while q:
	ck, ci, cj = q.popleft()
	for p in range(6):
		ni, nk, nj = ci + di[p], ck + dk[p], cj + dj[p]
		if 0 <= ni < n and 0 <= nj < m and 0 <= nk < h and not visit[nk][ni][nj] and graph[nk][ni][nj] != -1:
			visit[nk][ni][nj] = visit[ck][ci][cj] + 1
			q.append([nk, ni, nj])

for k in range(h):
	for i in range(n):
		result = max(result, max(visit[k][i]) - 1)
		for j in range(m):
			if visit[k][i][j] == 0 and graph[k][i][j] == 0:
				print(-1)
				exit()

print(result)