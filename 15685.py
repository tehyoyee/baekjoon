# 15685.py
# 23.04.19. 10:31 ~ 12:00

import sys
from collections import deque
input = sys.stdin.readline

di = (0, -1, 0, 1)
dj = (1, 0, -1, 0)

result = 0
N = int(input())
graph = [deque([]) for _ in range(4)]
visit = [[False] * (101) for _ in range(101)]
gMax = [0] * 4

for _ in range(N):
	x, y, d, g = map(int, input().split())
	gMax[d] = max(gMax[d], g)
	graph[d].append([x, y, g])

path = [[i] for i in range(4)]
for k in range(4):
	for i in range(1, gMax[k] + 1):
		for j in range(len(path[k]) - 1, -1, -1):
			path[k].append((path[k][j] + 1) % 4)
for k in range(4):
	while graph[k]:
		cj, ci, cg = graph[k].popleft()
		ni = ci
		nj = cj
		visit[ni][nj] = True
		for i in range(1, 2 ** cg + 1):
			ni = ni + di[path[k][i - 1]]
			nj = nj + dj[path[k][i - 1]]
			visit[ni][nj] = True
for i in range(0, 100):
	for j in range(0, 100):
		if visit[i][j] and visit[i + 1][j] and visit[i][j + 1] and visit[i + 1][j + 1]:
			result += 1
print(result)