# 1005.py
# 23.07.12. 15:59 ~ 16:15

import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
	N, K = map(int, input().split())
	buildings = [0] + list(map(int, input().split()))
	graph = [[] for _ in range(N + 1)]
	graphReverse = [[] for _ in range(N + 1)]
	topol = [0] * (N+1)

	visit = [False] * (N+1)
	q = deque([])
	for _ in range(K):
		a, b = map(int, input().split())
		graph[a].append(b)
		graphReverse[b].append(a)
		topol[b] += 1
	W = int(input())

	for i in range(1, N+1):
		if topol[i] == 0:
			q.append(i)
			visit[i] = True
	while q:
		ci = q.popleft()

		if ci == W:
			break
		for ni in graph[ci]:
			topol[ni] -= 1
		for i in range(1, N+1):
			if not visit[i] and topol[i] == 0:
				tmp = []
				for x in graphReverse[i]:
					tmp.append(buildings[x])
				buildings[i] += max(tmp)
				visit[i] = True
				q.append(i)
		
	print(buildings[W])