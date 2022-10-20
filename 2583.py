# 2583.py

# 22:20 ~

import sys
input = sys.stdin.readline

# di = [1, 1, -1, -1]
# dj = [1, -1, 1, -1]

# def bfs(graph, i, j):
# 	result = 0
# 	queue = [[j, i]]
# 	while queue:
# 		v_i, v_j = queue.pop(0)
# 		for k in range(4):
# 			if 0 <= v_i + di[k] < n and 0 <= v_j + dj[k] < m and not graph[v_i + di[k]][v_j + dj[k]]:
# 				queue.append([v_i + di[k], v_j + dj[k]])
# 				graph[v_i + di][v_j + dj] = 1
# 				result += 1
				

# def set_rect(rect, graph):
# 	for i in range(rect[0], rect[2]):
# 		for j in range(rect[1], rect[3]):
# 			graph[j][i] = 1

# m, n, k = map(int, input().split())
# rect = []
# graph = [[0] * n for _ in range(m)]
# result_cnt = 0
# result_size = []
# for _ in range(k):
# 	set_rect(list(map(int, input().split())), graph)
# print(graph)

# for m in range(m):
# 	for n in range(n):
# 		if not graph[m][n]:
# 			result_cnt += 1
# 			result_size.append(bfs(graph.copy(), n, m))
# print(graph)
# print(result_cnt)
# print(result_size)


import sys
input = sys.stdin.readline

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(graph):
	result_cnt = 0
	result_size =[]
	size = 0
	for i in range(m):
		for j in range(n):
			if size:
				result_size.append(size)
			size = 0
			if graph[i][j] == 1:
				continue
			result_cnt += 1
			queue = [[i, j]]
			size += 1
			while queue:
				v_i = queue[0][0]
				v_j = queue[0][1]
				queue.pop(0)
				graph[v_i][v_j] = 1
				for k in range(4):
					if 0 <= v_i + di[k] < m and 0 <= v_j + dj[k] < n and not graph[v_i + di[k]][v_j + dj[k]]:
						queue.append([v_i + di[k], v_j + dj[k]])
						graph[v_i + di[k]][v_j + dj[k]] = 1
						size += 1
	result_size.sort()
	print(result_cnt)
	for z in result_size:
		print(z, end = ' ')

def set_rect(rect, graph):
	for i in range(rect[0], rect[2]):
		for j in range(rect[1], rect[3]):
			graph[j][i] = 1

m, n, k = map(int, input().split())
rect = []
graph = [[0] * n for _ in range(m)]
result_cnt = 0
result_size = []
for _ in range(k):
	set_rect(list(map(int, input().split())), graph)
bfs(graph)