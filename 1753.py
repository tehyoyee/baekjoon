# 1753.py
# 23.03.29. 11:20 ~ 11:30

import sys
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
	u, v, w = map(int, input().split())
	graph[u].append((v, w))

dp = [10000000] * (V + 1)
dp[K] = 0

q = []
heapq.heappush(q, (0, K))
while q:
	cur_cost, cur_i = heapq.heappop(q)
	if cur_cost > dp[cur_i]:
		continue
	for new_i, next_cost in graph[cur_i]:
		new_cost = next_cost + cur_cost
		if new_cost < dp[new_i]:
			dp[new_i] = new_cost
			heapq.heappush(q, (new_cost, new_i))

for x in range(1, V + 1):
	if dp[x] == 10000000:
		print("INF")
	else:
		print(dp[x])
