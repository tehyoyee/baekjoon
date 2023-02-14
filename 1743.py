# 1743.py
# 23.02.14. 20:49 ~

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n, m, k = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
visit = [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(k):
	a, b = map(int, input().split())
	graph[a][b] = 1

def bfs(i, j):
	size = 0
	visit[i][j] = 1
	q = [[i, j]]
	while q:
		ni, nj = q.pop(0)
		for k in range(4):
			if not (1 <= ni + di[k] < n + 1 and 1 <= nj + dj[k] < m + 1):
				continue
			if graph[ni + di[k]][nj + dj[k]] and not visit[ni + di[k]][nj + dj[k]]:
				q.append([ni + di[k], nj + dj[k]])
				visit[ni + di[k]][nj + dj[k]] = 1
				size += 1
	print(size)
	return size
result = 0
for i in range(0, n + 1):
	for j in range(0, m + 1):
		if not visit[i][j]:
			result = max(result, bfs(i, j))

print(result)