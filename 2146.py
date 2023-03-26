# 2146.py
# 23.03.26. 18:47 ~ 19:30 21:42

# di = [0, 0, 1, -1]
# dj = [1, -1, 0, 0]

# import sys
# input = sys.stdin.readline
# from collections import deque

# def bfs(q, i, j, N, color):
# 	# q = deque([[i, j]])
# 	while q:
# 		ci, cj = q.popleft();
# 		for k in range(4):
# 			ni, nj = ci + di[k], cj + dj[k]
# 			if 0 <= ni < N and 0 <= nj < N:
# 				if graph[ni][nj] < 0 and graph[ni][nj] != color:
# 					print(ni, nj)
# 					return graph[ci][cj]
# 				elif graph[ni][nj] == 0:
# 					graph[ni][nj] = graph[ci][cj] + 1
# 				q.append([ni, nj])


# def colorBfs(i, j, N, color):
# 	q = deque([[i, j]])
# 	while q:
# 		ci, cj = q.popleft();
# 		for k in range(4):
# 			ni, nj = ci + di[k], cj + dj[k]
# 			if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] == 1:
# 				graph[ni][nj] = color
# 				q.append([ni, nj])

# result = 1000
# N = int(input())
# graph = []
# visit = [[0] * N for _ in range(N)]
# for _ in range(N):
#     graph.append(list(map(int, input().split())))
# color = -1
# for i in range(N):
# 	for j in range(N):
# 		if graph[i][j] == 1:
# 			graph[i][j] = color
# 			colorBfs(i, j, N, color)
# 			color -= 1
# q = deque([])
# colorCnt = color
# color = -1
# while colorCnt != color:
# 	for i in range(N):
# 		for j in range(N):
# 			if graph[i][j] == 0:
# 				for k in range(4):
# 					ni, nj = i + di[k], j + dj[k]
# 					if 0 <= ni < N and 0 <= nj < N:
# 						if graph[ni][nj] == color:
# 							graph[i][j] = 1
# 							q.append([i, j])
# 	result = min(bfs(q, i, j, N, color), result)
# 	color -= 1


# print(result)
# for x in graph:
# 	print(x)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

def bfs(q, N):
	while q:
		ci, cj, color = q.popleft();
		for k in range(4):
			ni, nj = ci + di[k], cj + dj[k]
			if 0 <= ni < N and 0 <= nj < N:
				if graph[ni][nj] < 0 and graph[ni][nj] != color:
					return graph[ci][cj]
				elif graph[ni][nj] == 0:
					graph[ni][nj] = graph[ci][cj] + 1
				q.append([ni, nj, color])
	return 1000

def colorBfs(i, j, N, color):
	q = deque([[i, j]])
	while q:
		ci, cj = q.popleft();
		for k in range(4):
			ni, nj = ci + di[k], cj + dj[k]
			if 0 <= ni < N and 0 <= nj < N and Ograph[ni][nj] == 1:
				Ograph[ni][nj] = color
				q.append([ni, nj])
	return 10000

result = 1000
N = int(input())
Ograph = []
for _ in range(N):
    Ograph.append(list(map(int, input().split())))
color = -1
for i in range(N):
	for j in range(N):
		if Ograph[i][j] == 1:
			Ograph[i][j] = color
			colorBfs(i, j, N, color)
			color -= 1
graph = deepcopy(Ograph)
colorCnt = color
color = -1
while colorCnt != color:
	graph = deepcopy(Ograph)
	q = deque([])
	for i in range(N):
		for j in range(N):
			if graph[i][j] == 0:
				for k in range(4):
					ni, nj = i + di[k], j + dj[k]
					if 0 <= ni < N and 0 <= nj < N:
						if graph[ni][nj] == color:
							graph[i][j] = 1
							q.append([i, j, color])
	result = min(bfs(q, N), result)
	color -= 1


print(result)