# 24479.py
# 24.02.12. 20:30 ~ 20:40

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
global depth

def dfs(ci):
    global depth
    for ni in graph[ci]:
        if not visit[ni]:
            depth += 1
            visit[ni] = depth
            dfs(ni)

N, M, R = map(int, input().split())
# graph = [[False] * (N + 1) for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)
visit[R] = 1
depth = 1
for _ in range(M):
    a, b = map(int, input().split())
    # graph[a][b] = True
    # graph[b][a] = True
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort()
dfs(R)

for i in range(1, N+1):
    print(visit[i])