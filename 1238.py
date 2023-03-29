# 1238.py
# 23.03.29. 다익스트라 답지.

import sys
input = sys.stdin.readline
from collections import deque

result = 0
N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
	a, b, t = map(int, input().split())
	graph[a].append((b, t))

def dijkstra(i, X):
	q = deque([])
	time = [10000000] * (N + 1)
	time[i] = 0
	q.append((0, i))
	while q:
		ct, ci = q.popleft()
		if ct > time[ci]:
			continue
		for ni, t in graph[ci]:
			nt = ct + t
			if time[ni] > nt:
				time[ni] = nt
				q.append((nt, ni))
	return time[X]

for i in range(1, N + 1):
	result = max(result, (dijkstra(i, X) + dijkstra(X, i)))

print(result)
