# 16236.py
# 23.02.09. 10:20 ~ ?

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

def bfs(q, size, n):
	flag = 0
	candi = []
	tmp = q[0][2]
	visit = [[False] * n for _ in range(n)]
	while q:
		y, x, steps = q.pop(0)
		if 0 < graph[y][x] < size:
			candi.append([y, x, steps])
			flag = 1
		for k in range(4):
			if 0 <= y + di[k] < n and 0 <= x + dj[k] < n:
				if not flag and not visit[y + di[k]][x + dj[k]] and graph[y + di[k]][x + dj[k]] <= size:
					q.append([y + di[k], x + dj[k], steps + 1])
					visit[y + di[k]][x + dj[k]] = True
	if len(candi) == 0:
		return [-1, -1, tmp]
	candi.sort(key=lambda x:(x[2], x[0], x[1]))
	graph[candi[0][0]][candi[0][1]] = 0
	return [candi[0][0], candi[0][1], candi[0][2]]

n = int(input())
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))
	for j in range(n):
		if graph[i][j] == 9:
			y, x = i, j
			graph[i][j] = 0
eat = 0
steps, size = 0, 2
while True:
	y, x, steps = bfs([[y, x, steps]], size, n)
	if y == -1:
		print(steps)
		break
	eat += 1
	if size == eat:
		eat = 0
		size += 1	

#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################


# di = [-1, 0, 0, 1]
# dj = [0, -1, 1, 0]

# from collections import deque

# def bfs(q, size, n):
# 	flag = 0
# 	candi = []
# 	tmp = q[0][2]
# 	visit = [[False] * n for _ in range(n)]
# 	while q:
# 		# print(q)
# 		y, x, steps = q.pop(0)
# 		# print(y, x, steps)
# 		if 0 < graph[y][x] < size:
# 			candi.append([y, x, steps])
# 			# print("zzzzzzzzzz")
# 			flag = 1
# 			# graph[y][x] = 0
# 			# return [y, x, steps]
# 		# if direction == -1:
# 		for k in range(4):
# 			if 0 <= y + di[k] < n and 0 <= x + dj[k] < n:
# 				if not flag and not visit[y + di[k]][x + dj[k]] and graph[y + di[k]][x + dj[k]] <= size:
# 					q.append([y + di[k], x + dj[k], steps + 1, k])
# 					visit[y + di[k]][x + dj[k]] = True
# 	if len(candi) == 0:
# 		return [-1, -1, tmp]
# 	if len(candi) >= 1:
# 		candi.sort(key=lambda x:(x[2], x[0], x[1]))
# 		print("candi = ",  candi)
# 		graph[candi[0][0]][candi[0][1]] = 0
# 		return [candi[0][0], candi[0][1], candi[0][2]]
	
# 		# elif direction == 0:
# 		# 	for k in range(3):
# 		# 		if 0 <= y + di[k] < n and 0 <= x + dj[k] < n:
# 		# 			if not visit[y + di[k]][x + dj[k]] and graph[y + di[k]][x + dj[k]] <= size:
# 		# 				q.append([y + di[k], x + dj[k], steps + 1, k])
# 		# 				visit[y + di[k]][x + dj[k]] = True
# 		# elif direction == 1:
# 		# 	k = 1
# 		# 	if 0 <= y + di[k] < n and 0 <= x + dj[k] < n:
# 		# 		if not visit[y + di[k]][x + dj[k]] and graph[y + di[k]][x + dj[k]] <= size:
# 		# 			q.append([y + di[k], x + dj[k], steps + 1, k])
# 		# 			visit[y + di[k]][x + dj[k]] = True
# 		# elif direction == 2:
# 		# 	k = 2
# 		# 	if 0 <= y + di[k] < n and 0 <= x + dj[k] < n:
# 		# 		if not visit[y + di[k]][x + dj[k]] and graph[y + di[k]][x + dj[k]] <= size:
# 		# 			q.append([y + di[k], x + dj[k], steps + 1, k])
# 		# 			visit[y + di[k]][x + dj[k]] = True
# 		# elif direction == 3:
# 		# 	for k in range(1, 4):
# 		# 		if 0 <= y + di[k] < n and 0 <= x + dj[k] < n:
# 		# 			if not visit[y + di[k]][x + dj[k]] and graph[y + di[k]][x + dj[k]] <= size:
# 		# 				q.append([y + di[k], x + dj[k], steps + 1, k])
# 		# 				visit[y + di[k]][x + dj[k]] = True

# 	# return [-1, -1, tmp]

# n = int(input())
# graph = []				# 맵
# for i in range(n):
# 	graph.append(list(map(int, input().split())))
# 	for j in range(n):
# 		if graph[i][j] == 9:
# 			y = i
# 			x = j
# 			graph[i][j] = 0
# eat = 0
# steps, size = 0, 2
# while True:
# 	# print("qwer")
# 	y, x, steps = bfs([[y, x, steps, 0]], size, n)
# 	print("end", y,x,steps, size)
# 	if y == -1:
# 		print(steps)
# 		break
# 	eat += 1
# 	if size == eat:
# 		eat = 0
# 		size += 1	
# y, x, steps, size = bfs([[y, x, steps, size]], n)
# if y == -1:
# 	print(steps)
# 	# break
# 	eat += 1
# 	if size == eat:
# 		eat = 0
# 		size += 1
# 	for j in range(n):
# 		if 0 < graph[i][j]:
# 			fishes.append([i, j, graph[i][j]])
# fishes.sort(key=lambda x:(x[2], x[0], x[1]))
# q = deque([fishes.pop()])
# q[0][2] = 2
# print(q[0][0], q[0][1])
# for x in fishes:
# 	print(x)
# print()
# while q:
# 	y, x, size = q.pop()
# 	candi = []
# 	for i in range(len(fishes)):
# 		if fishes[i][2] < size:
# 			candi.append(i)
# 		else:
# 			break
# 	target_idx = candi[0]
# 	if len(candi) == 0:
# 		break
# 	elif len(candi) > 1:
# 		d = abs(y - fishes[candi[0]][0]) + abs(x - fishes[candi[0]][1])
# 		for i in candi:
# 			if d > abs(y - fishes[i][0]) + abs(x - fishes[i][1]):
# 				d = abs(y - fishes[i][0]) + abs(x - fishes[i][1])
# 				target_idx = i
	# if len(candi) > 1:
	# 	d = 1000
	# 	for i in len(candi):
	# 		tmp = abs([i][0] - y) + abs(candi[i][1] - x)
	# 		if tmp < d:
	# 			d = tmp
	# 			target_index = i

			