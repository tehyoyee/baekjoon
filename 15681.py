# 15681.py
# 23.03.20. 10:11 ~ 10:28

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i):
	for ni in graph[i]:
		if not visit[ni]:
			visit[ni] += 1
			visit[i] += dfs(ni)
	return visit[i]

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visit[R] = 1
dfs(R)
for _ in range(Q):
	print(visit[int(input())])