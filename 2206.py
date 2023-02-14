# 2206.py
# 23.02.14. 16:52 ~ 17:52, 18:59 ~

# result = 1000000
# di = [0, 0, 1, -1]
# dj = [1, -1, 0, 0]

# n, m = map(int, input().split())
# graph = []
# for i in range(n):
# 	graph.append(list(map(int, input())))
# visit1 = [[0] * m for _ in range(n)]
# visit2 = [[0] * m for _ in range(n)]
# q = [[0, 0, 1]]
# visit1[0][0] = 1
# while q:
# 	i_c, j_c, steps = q.pop(0)
# 	if not (i_c == n - 1 and j_c == m - 1):
# 		for k in range(4):
# 			if 0 <= i_c + di[k] < n and 0 <= j_c + dj[k] < m and not visit1[i_c + di[k]][j_c + dj[k]]:
# 				if graph[i_c + di[k]][j_c + dj[k]] != 0:
# 					visit1[i_c + di[k]][j_c + dj[k]] = steps + 1
# 				else:
# 					q.append([i_c + di[k], j_c + dj[k], steps + 1])
# 					visit1[i_c + di[k]][j_c + dj[k]] = steps + 1

# q = [[n - 1, m - 1, 1]]
# visit2[n - 1][m - 1] = 1
# while q:
# 	i_c, j_c, steps = q.pop(0)
# 	for k in range(4):
# 		if 0 <= i_c + di[k] < n and 0 <= j_c + dj[k] < m and visit2[i_c + di[k]][j_c + dj[k]] == 0:
# 			if graph[i_c + di[k]][j_c + dj[k]] != 0:
# 				visit2[i_c + di[k]][j_c + dj[k]] = steps + 1
# 			else:
# 				q.append([i_c + di[k], j_c + dj[k], steps + 1])
# 				visit2[i_c + di[k]][j_c + dj[k]] = steps + 1

# for i in range(n):
# 	for j in range(m):
# 		if visit1[i][j] and visit2[i][j]:
# 			result = min(result, visit1[i][j] + visit2[i][j] - 1)
# if result == 1000000:
# 	print(-1)
# else:
# 	print(result)

# di = [0, 0, 1, -1]
# dj = [1, -1, 0, 0]

# n, m = map(int, input().split())
# graph = []
# result = -1
# for i in range(n):
# 	graph.append(list(map(int, input())))

# visit = [[[False] * 2 for _ in range(m)] for _ in range(n)]
# q = [[0, 0, 1, 1]]
# visit[0][0][0] = True
# visit[0][0][1] = True
# while q:
# 	i_c, j_c, steps, chance = q.pop(0)
# 	print(i_c, j_c, steps, chance)
# 	for x in visit:
# 		print(x)
# 	if i_c == n - 1 and j_c == m - 1:
# 		result = steps
# 	else:
# 		for k in range(4):
# 			if 0 <= i_c + di[k] < n and 0 <= j_c + dj[k] < m and not visit[i_c + di[k]][j_c + dj[k]][0]:
# 				if graph[i_c + di[k]][j_c + dj[k]] == 1 and chance == 1:
# 					q.append([i_c + di[k], j_c + dj[k], steps + 1, 0])
# 					visit[i_c + di[k]][j_c + dj[k]][0] = True
# 				elif graph[i_c + di[k]][j_c + dj[k]] == 0:
# 					q.append([i_c + di[k], j_c + dj[k], steps + 1, chance])
# 					visit[i_c + di[k]][j_c + dj[k]][0] = True
# 			elif 0 <= i_c + di[k] < n and 0 <= j_c + dj[k] < m and not visit[i_c + di[k]][j_c + dj[k]][1]:
# 				if graph[i_c + di[k]][j_c + dj[k]] == 0:
# 					q.append([i_c + di[k], j_c + dj[k], steps + 1, chance])
# 					visit[i_c + di[k]][j_c + dj[k]][1] = True
			

# print(result)


# di = [0, 0, 1, -1]
# dj = [1, -1, 0, 0]

# n, m = map(int, input().split())
# graph = []
# result = -1
# for i in range(n):
# 	graph.append(list(map(int, input())))
# visit = [[False] * m for _ in range(n)]
# q = [[0, 0, 1, 1]]
# visit[0][0] = True
# while q:
# 	i_c, j_c, steps, chance = q.pop(0)
# 	if i_c == n - 1 and j_c == m - 1:
# 		result = steps
# 	else:
# 		for k in range(4):
# 			if 0 <= i_c + di[k] < n and 0 <= j_c + dj[k] < m and not visit[i_c + di[k]][j_c + dj[k]]:
# 				if graph[i_c + di[k]][j_c + dj[k]] == 1 and chance == 1:
# 					q.append([i_c + di[k], j_c + dj[k], steps + 1, 0])
# 					visit[i_c + di[k]][j_c + dj[k]] = True
# 				elif graph[i_c + di[k]][j_c + dj[k]] == 0:
# 					q.append([i_c + di[k], j_c + dj[k], steps + 1, chance])
# 					visit[i_c + di[k]][j_c + dj[k]] = True

# print(result)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n, m = map(int, input().split())
graph = []
result = -1
for i in range(n):
	graph.append(list(map(int, input())))

visit = [[[False] * 2 for _ in range(m)] for _ in range(n)]
q = [[0, 0, 1, 1]]
visit[0][0][0] = True
visit[0][0][1] = True
while q:
	i_c, j_c, steps, chance = q.pop(0)
	print(i_c, j_c, steps, chance)
	for x in visit:
		print(x)
	if i_c == n - 1 and j_c == m - 1:
		result = steps
	else:
		for k in range(4):
			if not (0 <= i_c + di[k] < n and 0 <= j_c + dj[k] < m):
				continue
			if chance == 1:
				if graph[i_c + di[k]][j_c + dj[k]] == 1:
					if not visit[i_c + di[k]][j_c + dj[k]][0]:




			if 0 <= i_c + di[k] < n and 0 <= j_c + dj[k] < m and not visit[i_c + di[k]][j_c + dj[k]][0]:
				if graph[i_c + di[k]][j_c + dj[k]] == 1 and chance == 1:
					q.append([i_c + di[k], j_c + dj[k], steps + 1, 0])
					visit[i_c + di[k]][j_c + dj[k]][0] = True
				elif graph[i_c + di[k]][j_c + dj[k]] == 0:
					q.append([i_c + di[k], j_c + dj[k], steps + 1, chance])
					visit[i_c + di[k]][j_c + dj[k]][0] = True
			elif 0 <= i_c + di[k] < n and 0 <= j_c + dj[k] < m and not visit[i_c + di[k]][j_c + dj[k]][1]:
				if graph[i_c + di[k]][j_c + dj[k]] == 0:
					q.append([i_c + di[k], j_c + dj[k], steps + 1, chance])
					visit[i_c + di[k]][j_c + dj[k]][1] = True
			

print(result)