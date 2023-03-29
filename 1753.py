# 1753.py
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())
dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]
def Dijkstra(start):
	dp[start] = 0
	heapq.heappush(heap,(0, start))
	while heap:
		print(heap)
		wei, now = heapq.heappop(heap)
		if dp[now] < wei:
			continue
		for w, next_node in graph[now]:
			next_wei = w + wei
			if next_wei < dp[next_node]:
				dp[next_node] = next_wei
				heapq.heappush(heap,(next_wei,next_node))
for _ in range(E):
	u, v, w = map(int, input().split())
	graph[u].append((w, v))


Dijkstra(K)
for i in range(1,V+1):
	print("INF" if dp[i] == INF else dp[i])


# import sys
# import math
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def dfs(cur):
# 	print(cur)
# 	for x in graph[cur]:
# 		if w[x[0]] < w[cur] + x[1]:
# 			continue
# 		w[x[0]] = w[cur] + x[1]
# 		dfs(x[0])

# v, e = map(int, input().split())
# s = int(input())
# graph = [[] for _ in range(v + 1)]
# w = [math.inf for _ in range(v + 1)]
# for _ in range(e):
# 	a, b, c = map(int, input().split())
# 	graph[a].append([b, c])

# w[s] = 0
# dfs(s)
# for x in range(1, v + 1):
# 	print("INF") if w[x] == math.inf else print(w[x])