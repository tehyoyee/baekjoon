# 1238.py
# 23.03.09. 17:02 ~ 17:41

# import sys
# input = sys.stdin.readline

# def dfs(i, x, cost, n):
# 	result = 1000000000
# 	if i == x:
# 		return cost
# 	for ni in range(1, n + 1):
# 		if graph[i][ni] and not visit[ni]:
# 			visit[ni] = 1
# 			result = min(dfs(ni, x, cost + graph[i][ni], n), result)
# 			visit[ni] = 0
# 	return result

# N, M, X = map(int, input().split())
# result = [0] * (N + 1)
# graph = [[0] * (N + 1) for _ in range(N + 1)]
# visit = [0] * (N + 1)
# for _ in range(M):
# 	a, b, c = map(int, input().split())
# 	graph[a][b] = c
# for start in range(1, N + 1):
# 	result[start] += (dfs(start, X, 0, N))
# for start in range(1, N + 1):
# 	result[start] += (dfs(X, start, 0, N))
# print(max(result))

import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
result = [0] * (N + 1)
graph = [[float("inf")] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
	a, b, c = map(int, input().split())
	graph[a][b] = c
for x in graph:
	print(x)
print()
for k in range(1, N + 1):
	for i in range(1, N + 1):
		for j in range(1, N + 1):
			graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
for i in range(1, N + 1):
	result[i] += (graph[i][X] + graph[X][i])
for x in graph:
	print(x)
print(max(result))