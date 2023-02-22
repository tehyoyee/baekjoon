# 17070.py
# 23.02.22 16:26 ~  

# di = [0, 1, 1]	#가로 세로 대각선
# dj = [1, 0, 1]
# global result
# result = 0
# def is_row(i, j, d):
# 	if d == 1 or not 0 <= j < n - 1 or graph[i][j + 1] > 0:
# 		return False
# 	return True

# def is_col(i, j, d):
# 	if d == 0 or not 0 <= i < n - 1 or graph[i + 1][j] > 0:
# 		return False
# 	return True

# def is_diagonal(i, j):
# 	if (not (0 <= i < n - 1 and 0 <= j < n - 1)):
# 		return False
# 	for k in range(3):
# 		if graph[i + di[k]][j + dj[k]] > 0:
# 			return False
# 	return True

# def dfs(i, j, d, n):
# 	global result
# 	if i == n - 1 and j == n - 1:
# 		result += 1
# 	if is_row(i, j, d):
# 		graph[i][j + 1] += graph[i][j]
# 		dfs(i, j + 1, 0, n)
# 	if is_col(i, j, d):
# 		graph[i + 1][j] += graph[i][j]
# 		dfs(i + 1, j, 1, n)
# 	if is_diagonal(i, j):
# 		graph[i + 1][j + 1] += graph[i][j]
# 		dfs(i + 1, j + 1, 2, n)

# n = int(input())
# graph = []
# for _ in range(n):
# 	graph.append(list(map(int, input().split())))
# graph[0][1] = -1
# dfs(0, 1, 0, n)
# print(result)

# from collections import deque
# di = [0, 1, 1]	#가로 세로 대각선
# dj = [1, 0, 1]

# result = 0
# def is_row(i, j, d):
# 	if d == 1 or not 0 <= j < n - 1 or graph[i][j + 1] == 1:
# 		return False
# 	return True

# def is_col(i, j, d):
# 	if d == 0 or not 0 <= i < n - 1 or graph[i + 1][j] == 1:
# 		return False
# 	return True

# def is_diagonal(i, j):
# 	if not (0 <= i < n - 1 and 0 <= j < n - 1):
# 		return False
# 	for k in range(3):
# 		if graph[i + di[k]][j + dj[k]] == 1:
# 			return False
# 	return True

# n = int(input())
# graph = []
# for _ in range(n):
# 	graph.append(list(map(int, input().split())))
# q = deque([[0, 1, 0]])
# while q:
# 	ci, cj, cd = q.popleft()
# 	if ci == n - 1 and cj == n - 1:
# 		result += 1
# 	else:
# 		if is_row(ci, cj, cd):
# 			q.append([ci, cj + 1, 0])
# 		if is_col(ci, cj, cd):
# 			q.append([ci + 1, cj, 1])
# 		if is_diagonal(ci, cj):
# 			q.append([ci + 1, cj + 1, 2])
# print(result)



from collections import deque

result = 0
n = int(input())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
q = deque([[0, 0, 0]])
while q:
	ci, cj, cd = q.popleft()
	if ci == n - 1 and cj == n - 1:
		result += 1
	else:
		if 0 <= ci < n - 1 and 0 <= cj < n - 1 and graph[ci][cj + 1] == 0 and graph[ci + 1][cj] == 0 and graph[ci + 1][cj + 1] == 0:
			q.append([ci + 1, cj + 1, 2])
			if cd != 1:
				q.append([ci, cj + 1, 0])
			if cd != 0:
				q.append([ci + 1, cj, 1])
		else:
			if cd != 1 and 0 <= cj < n - 1 and graph[ci][cj + 1] == 0:
				q.append([ci, cj + 1, 0])
			if cd != 0 and 0 <= ci < n - 1 and graph[ci + 1][cj] == 0:
				q.append([ci + 1, cj, 1])
print(result)

