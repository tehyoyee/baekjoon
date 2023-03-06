# 6593.py
# 23.03.06. 11:23 ~ 11:57 13:28 ~ 13:43

di = [0, 0, 0, 0, 1, -1]
dj = [1, -1, 0, 0, 0, 0]
dk = [0, 0, 1, -1, 0, 0]

import sys
from collections import deque
input = sys.stdin.readline

while True:
	s = []
	e = []
	L, R, C = map(int, input().split())
	graph = [[[] for _ in range(R)] for _ in range(L)]
	visit = [[[-1] * (C) for _ in range(R)] for _ in range(L)]
	if L == 0 and R == 0 and C == 0:
		break
	for i in range(L):
		for j in range(R):
			graph[i][j] = (list(input().rstrip()))
			for k in range(C):
				if graph[i][j][k] == 'S':
					s = [i, j, k]
				elif graph[i][j][k] == 'E':
					e = [i, j, k]
		a = input()
	q = deque([s])
	visit[s[0]][s[1]][s[2]] = 0
	flag = 1
	while q:
		ci, cj, ck = q.popleft()
		if ci == e[0] and cj == e[1] and ck == e[2]:
			print("Escaped in", visit[ci][cj][ck], "minute(s).")
			flag = 0
			break
		for d in range(6):
			ni, nj, nk = ci + di[d], cj + dj[d], ck + dk[d]
			if 0 <= ni < L and 0 <= nj < R and 0 <= nk < C and graph[ni][nj][nk] != '#' and visit[ni][nj][nk] == -1:
				visit[ni][nj][nk] = visit[ci][cj][ck] + 1
				q.append([ni, nj, nk])
	if flag:
		print("Trapped!")