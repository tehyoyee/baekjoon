# 1916.py
# 23.04.25. 09:21 ~ 09:41 INF값 작게 해서 틀렸다하네. 빡...

import sys
import heapq
input = sys.stdin.readline

INF = int(1e10)
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

start, end = map(int, input().split())

dp = [INF] * (N + 1)
dp[start] = 0
q = []
heapq.heappush(q, (0, start))
while q:
	curCost, curPos = heapq.heappop(q)
	if dp[curPos] < curCost:
		continue
	for newPos, addCost in graph[curPos]:
		newCost = curCost + addCost
		if dp[newPos] > newCost:
			dp[newPos] = newCost
			heapq.heappush(q, (newCost, newPos))
print(dp[end])