# 2206.py
# 23.02.14. 16:52 ~ 17:52, 18:59 ~ ? 16:14

import sys
from collections import deque
input = sys.stdin.readline

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(y, x):
	q = deque([[y, x, 1]])
	while q:
		i_c, j_c, c = q.popleft()
		if i_c == n - 1 and j_c == m - 1:
			return visit[i_c][j_c][c]
		else:
			for k in range(4):
				if not (0 <= i_c + di[k] < n and 0 <= j_c + dj[k] < m):
					continue
				if graph[i_c + di[k]][j_c + dj[k]] == 1 and c == 1:
					visit[i_c + di[k]][j_c + dj[k]][0] = visit[i_c][j_c][1] + 1
					q.append([i_c + di[k], j_c + dj[k], 0])
				elif graph[i_c + di[k]][j_c + dj[k]] == 0 and visit[i_c + di[k]][j_c + dj[k]][c] == 0:
					visit[i_c + di[k]][j_c + dj[k]][c] = visit[i_c][j_c][c] + 1
					q.append([i_c + di[k], j_c + dj[k], c])
	return -1

n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input().rstrip())))
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
q = deque([[0, 0, 1]])

visit[0][0][1] = 1
visit[0][0][0] = 1
print(bfs(0, 0))