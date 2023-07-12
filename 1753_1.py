# 1753.py

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
	u, v, w = map(int, input().split())
	graph[u].append((v, w))
	# graph[v].append((u, w))
INF = 10000000000
q = []
visit = [INF] * 6
visit[1] = 0
heapq.heappush(q, (K, 0))

while q:
	ci, cost = heapq.heappop(q)
	if (cost > visit[ci]):
		continue
	for ni, w in graph[ci]:
		if visit[ci] + w < visit[ni]:
			visit[ni] = visit[ci] + w
			heapq.heappush(q, (ni, visit[ni]))

print(visit)