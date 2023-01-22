# 1926.py
# 23.01.19. 21:06 ~

import sys
input = sys.stdin.readline

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n, m = map(int, input().split())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))

def bfs(i, j):
	q = [[i, j]]
	graph[i][j] = 0
	area = 0
	while q:
		a, b = q.pop(0)
		area += 1
		for k in range(4):
			if 0 <= a + di[k] < n and 0 <= b + dj[k] < m and graph[a + di[k]][b + dj[k]] == 1:
				q.append([a + di[k], b + dj[k]])
				graph[a + di[k]][b + dj[k]] = 0
	return area
cnt = 0
area_max = 0
for i in range(n):
	for j in range(m):
		if graph[i][j] == 1:
			cnt += 1
			area_max = max(area_max, bfs(i, j))
print(cnt)
print(area_max)