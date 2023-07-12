# 2638.py
# 23.07.06. 15:53 ~ 17:13

import sys
input = sys.stdin.readline
from collections import deque

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

N, M = map(int, input().split())
graph = []
visit = [[False] * M for _ in range(N)]
cheeze = deque()

for i in range(N):
	graph.append(list(map(int, input().split())))
	for j in range(M):
		if graph[i][j] == 1:
			cheeze.append((i, j))

def check(i, j):
	cnt = 0
	for k in range(4):
		ni, nj = i + di[k], j + dj[k]
		if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] and not graph[ni][nj]:
			cnt += 1
	if cnt >= 2:
		return True
	return False

def bfs(i, j):
	q = deque([(i, j)])
	while q:
		ci, cj = q.popleft()
		for k in range(4):
			ni, nj = ci + di[k], cj + dj[k]
			if 0 <= ni < N and 0 <= nj < M and not visit[ni][nj] and not graph[ni][nj]:
				visit[ni][nj] = True
				q.append((ni, nj))

result = 0
spreadAirCandi = deque([(0, 0)])
while cheeze:
	while spreadAirCandi:
		i, j = spreadAirCandi.popleft()
		visit[i][j] = True
		graph[i][j] = 0
		bfs(i, j)
	for l in range(len(cheeze)):
		i, j = cheeze.popleft()
		if check(i, j):
			spreadAirCandi.append((i, j))
		else:
			cheeze.append((i, j))
	result += 1

print(result)