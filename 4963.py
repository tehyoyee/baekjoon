# 4963 py

# 20:00 - 20:45

# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(graph, w, h):
# 	result = 0
# 	for i in range(h):
# 		for j in range(w):
# 			if graph[i][j] == 0:
# 				continue
# 			result += 1
# 			q_i = deque()
# 			q_j = deque()
# 			q_i.append(i)
# 			q_j.append(j)
# 			while q_i:
# 				v_i = q_i.popleft()
# 				v_j = q_j.popleft()
# 				graph[v_i][v_j] = 0
# 				if v_i - 1 >= 0:		# 12
# 					if graph[v_i - 1][v_j] == 1:
# 						q_i.append(v_i - 1)
# 						q_j.append(v_j)
# 				if v_i + 1 < h:
# 					if v_j + 1 < w:		# 2
# 						if graph[v_i - 1][v_j + 1] == 1:
# 							q_i.append(v_i - 1)
# 							q_j.append(v_j + 1)
# 					if v_j - 1 >= 0:		# 10
# 						if graph[v_i - 1][v_j - 1] == 1:
# 							q_i.append(v_i - 1)
# 							q_j.append(v_j - 1)			# 6
# 					if graph[v_i + 1][v_j] == 1:
# 						q_i.append(v_i + 1)
# 						q_j.append(v_j)
# 				if v_j - 1 >= 0:		# 9
# 					if graph[v_i][v_j - 1] == 1:
# 						q_i.append(v_i)
# 						q_j.append(v_j - 1)
# 				if v_j + 1 < w:		# 3
# 					if graph[v_i][v_j + 1] == 1:
# 						q_i.append(v_i)
# 						q_j.append(v_j + 1)
# 				if v_i + 1 < h:
# 					if v_j - 1 >= 0:		# 7
# 						if graph[v_i + 1][v_j - 1] == 1:
# 							q_i.append(v_i + 1)
# 							q_j.append(v_j - 1)
# 					if v_j + 1 < w:		# 5
# 						if graph[v_i + 1][v_j + 1] == 1:
# 							q_i.append(v_i + 1)
# 							q_j.append(v_j + 1)
# 	print(result)

# while (True):
# 	w, h = map(int, input().split())
# 	if (w == 0 and h == 0):
# 		break
# 	graph = []
# 	for _ in range(h):
# 		graph.append(list(map(int, input().split())))
# 	bfs(graph, w, h)


import sys
input = sys.stdin.readline

def bfs(graph, w, h):
	di = [-1, -1, 0, 1, 1, 1, 0, -1]
	dj = [0, -1, -1, -1, 0, 1, 1, 1]
	result = 0
	for i in range(h):
		for j in range(w):
			if graph[i][j] == 0:
				continue
			result += 1
			graph[i][j] = 0
			q = [[i, j]]
			while q:
				v_i = q[0][0]
				v_j = q[0][1]
				q.pop(0)
				for k in range(8):
					if 0 <= v_i + di[k] < h and 0 <= v_j + dj[k] < w and graph[v_i + di[k]][v_j +dj[k]]:
						q.append([v_i + di[k], v_j + dj[k]])
						graph[v_i + di[k]][v_j + dj[k]] = 0
	print(result)

while (True):
	w, h = map(int, input().split())
	if (w == 0 and h == 0):
		break
	graph = []
	for _ in range(h):
		graph.append(list(map(int, input().split())))
	bfs(graph, w, h)