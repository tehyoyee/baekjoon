# 16234.py
# 23.01.30. 10:08 ~

def bfs(i, j, cnt):
	area = 0
	total = 0
	q = [[i, j]]
	visit[i][j] = cnt
	while q:
		i_cur, j_cur = q.pop(0)
		total += graph[i_cur][j_cur]
		area += 1
		for k in range(4):
			if 0 <= i_cur + di[k] < n and 0 <= j_cur + dj[k] < n:
				if visit[i_cur + di[k]][j_cur + dj[k]] == 0 and l <= abs(graph[i_cur + di[k]][j_cur + dj[k]] - graph[i_cur][j_cur]) <= r:
					q.append([i_cur + di[k], j_cur + dj[k]])
					visit[i_cur + di[k]][j_cur + dj[k]] = cnt
	return cnt, total//area, area

def editGraph(cnt, value):
	for i in range(n):
		for j in range(n):
			if visit[i][j] == cnt:
				graph[i][j] = value
	return 1

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

n, l, r = map(int, input().split())
visit = [[0] * (n) for _ in range(n)]
graph = []
result = 0
for i in range(n):
	graph.append(list(map(int, input().split())))

while True:
	flag = 0
	cnt = 1
	visit = [[0] * (n) for _ in range(n)]
	for i in range(n):
		for j in range(n):
			if not visit[i][j]:
				cnt, value, area = bfs(i, j, cnt)
			if area != 1:
				flag = editGraph(cnt, value);
			cnt += 1
	if flag == 1:
		result += 1
	else:
		break

print(result)


# di = [1, -1, 0, 0]
# dj = [0, 0, 1, -1]

# n, l, r = map(int, input().split())
# visit = [[0] * (n) for _ in range(n)]
# graph = []
# tmp = []
# cnt = 1
# result = 0

# for i in range(n):
# 	graph.append(list(map(int, input().split())))

# def bfs(i, j, cnt):
# 	area = 0
# 	total = 0
# 	q = [[i, j]]
# 	visit[i][j] = cnt
# 	while q:
# 		i_cur, j_cur = q.pop(0)
# 		total += graph[i_cur][j_cur]
# 		area += 1
# 		for k in range(4):
# 			if 0 <= i_cur + di[k] < n and 0 <= j_cur + dj[k] < n:
# 				if visit[i_cur + di[k]][j_cur + dj[k]] < cnt and l <= abs(graph[i_cur + di[k]][j_cur + dj[k]] - graph[i_cur][j_cur]) <= r:
# 					q.append([i_cur + di[k], j_cur + dj[k]])
# 					visit[i_cur + di[k]][j_cur + dj[k]] = cnt
# 	return cnt, total//area, area

# def editGraph(arr):
# 	flag = 0
# 	while arr:
# 		cnt, v = arr.pop();
# 		for i in range(n):
# 			for j in range(n):
# 				if visit[i][j] == cnt:
# 					graph[i][j] = v
# 					flag = 1
# 	return flag

# while True:
# 	for i in range(n):
# 		for j in range(n):
# 			cnt, value, area = bfs(i, j, cnt)
# 			if area != 1:
# 				tmp.append([cnt, value])
# 			cnt += 1
# 	if editGraph(tmp) == 1:
# 		result += 1
# 	else:
# 		break
# print(result)