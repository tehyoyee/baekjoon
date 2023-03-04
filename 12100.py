# 12100.py
# 23.03.04. 10:01 ~

import copy

def toRight(graph, cnt, n):
	result = 0
	if cnt == 5:
		for x in graph:
			result = max(result, max(x))
		return result
	for i in range(n):
		tmp = -1
		nj = n - 1
		for j in range(n - 1, -1, -1):
			if graph[i][j]:
				if tmp != -1:
					if graph[i][j] == graph[i][tmp]:
						graph[i][nj] = graph[i][tmp] * 2
						graph[i][j] = 0
						if nj != tmp:
							graph[i][tmp] = 0
						tmp = -1
					else:
						nj -= 1
						if nj >= 0:
							graph[i][nj] = graph[i][j]
						tmp = j
					nj -= 1
				else:
					tmp = j
		if nj != tmp and tmp != -1 and nj >= 0:
			graph[i][nj], graph[i][tmp] = graph[i][tmp], 0
	for x in graph:
		print(x)
	print()
	result = max(result, toLower(graph, cnt + 1, n))
	# result = max(result, toLeft(graph, cnt + 1, n))
	# result = max(result, toUpper(graph, cnt + 1, n))
	return result

def toLeft(graph, cnt, n):
	result = 0
	if cnt == 5:
		for x in graph:
			result = max(result, max(x))
		return result
	for i in range(n):
		tmp = -1
		nj = 0
		for j in range(n):
			if graph[i][j]:
				if tmp != -1:
					if graph[i][j] == graph[i][tmp]:
						graph[i][nj] = graph[i][tmp] * 2
						graph[i][j] = 0
						if nj != tmp:
							graph[i][tmp] = 0
						tmp = -1
					else:
						nj += 1
						if nj < n:
							graph[i][nj] = graph[i][j]
						tmp = j
					nj += 1
				else:
					tmp = j
		if nj != tmp and tmp != -1 and nj < n:
			graph[i][nj], graph[i][tmp] = graph[i][tmp], 0
	for x in graph:
		print(x)
	print()
	# result = max(result, toLower(graph, cnt + 1, n))
	# result = max(result, toUpper(graph, cnt + 1, n))
	# result = max(result, toRight(graph, cnt + 1, n))
	return result

def toUpper(graph, cnt, n):
	result = 0
	if cnt == 5:
		for x in graph:
			result = max(result, max(x))
		return result
	for j in range(n):
		tmp = -1
		ni = 0
		for i in range(n):
			if graph[i][j]:
				if tmp != -1:
					if graph[i][j] == graph[tmp][j]:
						graph[ni][j] = graph[tmp][j] * 2
						graph[i][j] = 0
						if ni != tmp:
							graph[tmp][j] = 0
						tmp = -1
					else:
						ni += 1
						if ni < n:
							graph[ni][j] = graph[i][j]
						tmp = i
					ni += 1
				else:
					tmp = i
		if ni != tmp and tmp != -1 and ni < n:
			graph[ni][j], graph[tmp][j] = graph[tmp][j], 0
	for x in graph:
		print(x)
	print()
	# result = max(result, toLower(graph, cnt + 1, n))
	# result = max(result, toLeft(graph, cnt + 1, n))
	result = max(result, toRight(graph, cnt + 1, n))
	return result

def toLower(graph, cnt, n):
	result = 0
	if cnt == 5:
		for x in graph:
			result = max(result, max(x))
		return result
	for j in range(n):
		tmp = -1
		ni = n - 1
		for i in range(n - 1, -1, -1):
			if graph[i][j]:
				if tmp != -1:
					if graph[i][j] == graph[tmp][j]:
						graph[ni][j] = graph[tmp][j] * 2
						graph[i][j] = 0
						if ni != tmp:
							graph[tmp][j] = 0
						tmp = -1
					else:
						ni -= 1
						if ni >= 0:
							graph[ni][j] = graph[i][j]
						tmp = i
					ni -= 1
				else:
					tmp = i
		if ni != tmp and tmp != -1 and ni >= 0:
			graph[ni][j], graph[tmp][j] = graph[tmp][j], 0
	for x in graph:
		print(x)
	print()
	result = max(result, toLeft(graph, cnt + 1, n))
	# result = max(result, toUpper(graph, cnt + 1, n))
	# result = max(result, toRight(graph, cnt + 1, n))
	return result

n = int(input())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))

# print(toRight(copy.deepcopy(graph), 0, n))
print(toLeft(copy.deepcopy(graph), 0, n))
# print(toUpper(copy.deepcopy(graph), 0, n))
# print(toLower(copy.deepcopy(graph), 0, n))

# for x in graph:
	# print(x)