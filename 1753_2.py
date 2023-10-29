import sys
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())
K = int(input())
INF = 10000000
# graph = [[INF] * (V + 1) for _ in range(V + 1)]
graph = [[] for _ in range(V + 1)]
for _ in range(E):
	u, v, w = map(int, input().split())
	graph[u].append((v, w))

costs = [INF] * (V + 1)
costs[K] = 0
q = [(0, K)]

while q:
	cc, ci = heapq.heappop(q)
	if costs[ci] < cc:
		continue
	for ni, nc in graph[ci]:
		if cc + nc < costs[ni]:
			heapq.heappush(q, (cc + nc, ni))
			costs[ni] = cc + nc

for x in range(1, V + 1):
	if costs[x] == INF:
		print('INF')
	else:
		print(costs[x])