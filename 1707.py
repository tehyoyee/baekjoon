# 1707.py
# 23.04.06. 19:36 ~ 20:06

import sys
input = sys.stdin.readline
from collections import deque

K = int(input())
for _ in range(K):
	V, E = map(int, input().split())
	graph = [[] for _ in range(V + 1)]
	for _ in range(E):
		a, b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)

	visit = [-1] * (V + 1)
	result = "YES"
	for i in range(1, V + 1):
		if visit[i] == -1:
			visit[1] = 0
		q = deque([i])
		while q:
			cur = q.popleft()
			for new in graph[cur]:
				if visit[new] == -1:
					visit[new] = (visit[cur] + 1) % 2
					q.append(new)
				elif visit[new] == visit[cur]:
					result = "NO"
					break
	print(result)