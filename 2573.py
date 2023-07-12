# 2573.py
# 23.04.12. 15:42 ~

import sys
input = sys.stdin.readline
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def timegoes():
	q = []
	flag = 0
	for i in range(N):
		for j in range(M):
			cnt = 0
			if graph[i][j] == 0:
				continue
			for k in range(4):
				ni, nj = i + di[k], j + dj[k]
				if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 0:
					cnt += 1
			if cnt:
				q.append([i, j, cnt])
	if len(q):
		flag = 1
	for i, j, cnt in q:
		graph[i][j] -= cnt
		if graph[i][j] < 0:
			graph[i][j] = 0
	return flag		

def bfs(i, j, visit):
	q = deque([[i, j]])
	while q:
		ci, cj = q.popleft()
		for k in range(4):
			ni, nj = ci + di[k], cj + dj[k]
			if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] and not visit[ni][nj]:
				visit[ni][nj] = 1
				q.append([ni, nj])


def isPart():
	cnt = 0
	visit = [[0] * M for _ in range(N)]
	for i in range(N):
		for j in range(M):
			if graph[i][j] and not visit[i][j]:
				cnt += 1
				visit[i][j] = 1
				bfs(i, j, visit)
	if cnt >= 2:
		return True
	else:
		return False

result = 0
N, M = map(int, input().split())
graph = []
candi = deque([])
for i in range(N):
	graph.append(list(map(int, input().split())))
	for j in range(M):
		if graph[i][j]:
			candi.append([i, j])
flag = 1
while flag:
	flag = timegoes()
	result += 1
	if flag == 0:
		print(0)
		break
	if isPart():
		print(result)
		break