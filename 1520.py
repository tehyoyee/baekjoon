# 1520.py

# import sys
# input = sys.stdin.readline
# from collections import deque

# di = [0, 0, 1, -1]
# dj = [1, -1, 0, 0]

# def bfs(graph, n, m):
# 	s_map = [[0] * (m + 1) for _ in range(n + 1)]
# 	q = [[1, 1, graph[1][1]]]
# 	while q:
# 		i, j, h = q.pop(0)
# 		s_map[i][j] += 1
# 		for x in range(4):
# 			if 1 <= i + di[x] <= n and 1 <= j + dj[x] <= m and graph[i + di[x]][j + dj[x]] < h:
# 				q.append([i + di[x], j + dj[x], graph[i + di[x]][j + dj[x]]])
# 	print(s_map[n][m])

# n, m = map(int, input().split())
# graph = [[0] * (m + 1)]
# for i in range(n):
# 	graph.append([0] + list(map(int, input().split())))
# bfs(graph, n, m)

# import sys
# input = sys.stdin.readline
# from collections import deque

# di = [0, 0, 1, -1]
# dj = [1, -1, 0, 0]

# def bfs(graph, n, m):
# 	s_map = [[0] * (m + 1) for _ in range(n + 1)]
# 	q = deque([[1, 1, graph[1][1]]])
# 	while q:
# 		i, j, h = q.popleft()
# 		s_map[i][j] += 1
# 		for x in range(4):
# 			if 1 <= i + di[x] <= n and 1 <= j + dj[x] <= m and graph[i + di[x]][j + dj[x]] < h:
# 				q.append([i + di[x], j + dj[x], graph[i + di[x]][j + dj[x]]])
# 	print(s_map[n][m])

# n, m = map(int, input().split())
# graph = [[0] * (m + 1)]
# for i in range(n):
# 	graph.append([0] + list(map(int, input().split())))
# bfs(graph, n, m)

# import sys
# input = sys.stdin.readline
# from collections import deque

# di = [0, 0, 1, -1]
# dj = [1, -1, 0, 0]

# n, m = map(int, input().split())
# s_map = [[0] * (m) for _ in range(n)]
# graph = []
# for i in range(n):
# 	graph.append(list(map(int, input().split())))

# q = deque([[0, 0, graph[0][0]]])
# while q:
# 	i, j, h = q.popleft()
# 	s_map[i][j] += 1
# 	for x in range(4):
# 		if 0 <= i + di[x] < n and 0 <= j + dj[x] < m and graph[i + di[x]][j + dj[x]] < h:
# 			q.append([i + di[x], j + dj[x], graph[i + di[x]][j + dj[x]]])
# print(s_map[n - 1][m - 1])




# import sys
# input = sys.stdin.readline
# from collections import deque

# di = [0, 0, 1, -1]
# dj = [1, -1, 0, 0]

# result = 0
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
# 	graph.append(list(map(int, input().split())))

# q = deque([[0, 0, graph[0][0]]])
# while q:
# 	i, j, h = q.pop()
# 	if i == n - 1 and j == m - 1:
# 		result += 1
# 	for x in range(4):
# 		if 0 <= i + di[x] < n and 0 <= j + dj[x] < m and graph[i + di[x]][j + dj[x]] < h:
# 			q.append([i + di[x], j + dj[x], graph[i + di[x]][j + dj[x]]])
# print(result)
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# di = [0, 0, 1, -1]
# dj = [1, -1, 0, 0]

# n, m = map(int, input().split())
# s_map = [[-1] * (m) for _ in range(n)]
# graph = []
# for i in range(n):
# 	graph.append(list(map(int, input().split())))

# def dfs(i, j):
# 	if i == n - 1 and j == m - 1:
# 		return 1
# 	if s_map[i][j] != -1:
# 		return s_map[i][j]
# 	s_map[i][j] = 0
# 	h = graph[i][j]
# 	for x in range(4):
# 		if 0 <= i + di[x] < n and 0 <= j + dj[x] < m and graph[i + di[x]][j + dj[x]] < h:
# 			s_map[i][j] += dfs(i + di[x], j + dj[x])
# 	for x in s_map:
# 		print(x)
# 	print()
# 	return s_map[i][j]
# print(dfs(0, 0))


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n, m = map(int, input().split())
s_map = [[-1] * (m) for _ in range(n)]
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))
result = 0
def dfs(i, j, result):
	if i == n - 1 and j == m - 1:
		return 1
	if s_map[i][j] != -1:
		return s_map[i][j]
	s_map[i][j] = 0
	h = graph[i][j]
	for k in range(4):
		if 0 <= i + di[k] < n and 0 <= j + dj[k] < m and graph[i + di[k]][j + dj[k]] < h:
			s_map[i][j] += dfs(i + di[k], j + dj[k], result)
	return s_map[i][j]
print(dfs(0, 0, result))