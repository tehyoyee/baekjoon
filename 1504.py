# 1504.py
# 23.04.07. 19:38 ~ 19:57

import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

def dijkstra(start, target):
	dp = [100000000] * (N + 1)
	dp[start] = 0
	q = []
	heapq.heappush(q, [start, 0])
	while q:
		cur, cost = heapq.heappop(q)
		if cost > dp[cur]:
			continue
		for new, new_cost in graph[cur]:
			if dp[cur] + new_cost < dp[new]:
				dp[new] = dp[cur] + new_cost
				heapq.heappush(q, [new, dp[new]])
	if dp[target] == 100000000:
		print(-1)
		exit()
	return dp[target]

for _ in range(E):
	a, b, c = map(int, input().split())
	graph[a].append([b, c])
	graph[b].append([a, c])
v1, v2 = map(int, input().split())
A = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
B = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)