# 21608.py
# 23. 03. 09. 13:49 ~ 15:08

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

def search(n):
	candi = []
	point = 1000
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if point < graph[i][j]:
				candi = [[i, j]]
				point = graph[i][j]
			elif point == graph[i][j]:
				candi.append([i, j])
	return candi

def getRelationPoint(relation, n):
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if graph[i][j] < 1000:
				continue
			if graph[i][j] > 1000:
				graph[i][j] = 1000
			for k in range(4):
				ni, nj = i + di[k], j + dj[k]
				for r in relation:
					if graph[ni][nj] == r:
						graph[i][j] += 1

def considerAdjacent(n):
	new_candi = []
	point = 1000
	for c in candi:
		ci = c[0]
		cj = c[1]
		for k in range(4):
			ni, nj = ci + di[k], cj + dj[k]
			if graph[ni][nj] >= 1000:
				graph[ci][cj] += 1
		if graph[ci][cj] > point:
			new_candi = [[ci, cj]]
			point = graph[ci][cj]
		elif graph[ci][cj] == point:
			new_candi.append([ci, cj])
	return new_candi

result = 0
n = int(input())
relation = []
for _ in range(n ** 2):
	relation.append(list(map(int, input().split())))
graph = [[-1] * (n + 2)]

for _ in range(n):
	graph.append([-1] + [1000] * n + [-1])
graph.append([-1] * (n + 2))

for i in range(n ** 2):
	getRelationPoint(relation[i][1:], n)
	candi = search(n)
	if len(candi) != 1:
		candi = considerAdjacent(n)
	graph[candi[0][0]][candi[0][1]] = relation[i][0]
relation.sort()

for i in range(1, n + 1):
	for j in range(1, n + 1):
		tmp = 0
		for k in range(4):
			ni, nj = i + di[k], j + dj[k]
			if graph[ni][nj] in relation[graph[i][j] - 1][1:]:
				tmp += 1
		result += (10 ** tmp) // 10

print(result)