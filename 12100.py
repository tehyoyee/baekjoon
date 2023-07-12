# 12100.py
# 23.04.26. 09:23 ~ 10:40

import sys
input = sys.stdin.readline
from copy import deepcopy

N = int(input())
graph = []

def toLower(graph, N, cnt):
	newGraph = [[0] * N for _ in range(N)]
	for j in range(N):
		tmp = []
		tmp2 = []
		for i in range(N):
			if graph[i][j]:
				tmp.append(graph[i][j])
		i = len(tmp) - 1
		while i >= 0:
			if i == 0:
				tmp2.append(tmp[i])
				i -= 1
			elif tmp[i] != tmp[i - 1]:
				tmp2.append(tmp[i])
				i -= 1
			else:
				tmp2.append(tmp[i] * 2)
				i -= 2
		tmp2.reverse()
		tmp2 = [0] * (N - len(tmp2)) + tmp2
		for i in range(N):
			newGraph[i][j] = tmp2[i]
	return newGraph, cnt + 1


def toUpper(graph, N, cnt):
	newGraph = [[0] * N for _ in range(N)]
	for j in range(N):
		tmp = []
		tmp2 = []
		for i in range(N):
			if graph[i][j]:
				tmp.append(graph[i][j])
		i = 0
		while i < len(tmp):
			if i == len(tmp) - 1:
				tmp2.append(tmp[i])
				i += 1
			elif tmp[i] != tmp[i + 1]:
				tmp2.append(tmp[i])
				i += 1
			else:
				tmp2.append(tmp[i] * 2)
				i += 2
		tmp2 += [0] * (N - len(tmp2))
		for i in range(N):
			newGraph[i][j] = tmp2[i]
	return newGraph, cnt + 1

def toLeft(graph, N, cnt):
	newGraph = [[] for _ in range(N)]
	for i in range(N):
		tmp = []
		tmp2 = []
		for j in range(N):
			if graph[i][j]:
				tmp.append(graph[i][j])
		j = 0
		while j < len(tmp):
			if j == len(tmp) - 1:
				tmp2.append(tmp[j])
				j += 1
			elif tmp[j] != tmp[j + 1]:
				tmp2.append(tmp[j])
				j += 1
			else:
				tmp2.append(tmp[j] * 2)
				j += 2
		newGraph[i] = tmp2 + [0] * (N - len(tmp2))
	return newGraph, cnt + 1

def toRight(graph, N, cnt):
	newGraph = [[] for _ in range(N)]
	for i in range(N):
		tmp = []
		tmp2 = []
		for j in range(N):
			if graph[i][j]:
				tmp.append(graph[i][j])
		j = len(tmp) - 1
		while j >= 0:
			if j == 0:
				tmp2.append(tmp[j])
				j -= 1
			elif tmp[j] != tmp[j - 1]:
				tmp2.append(tmp[j])
				j -= 1
			else:
				tmp2.append(tmp[j] * 2)
				j -= 2
		tmp2.reverse()
		newGraph[i] = [0] * (N - len(tmp2)) + tmp2
	return newGraph, cnt + 1

for _ in range(N):
	graph.append(list(map(int, input().split())))

def dfs(cur, cnt, d):
	result = 0
	if cnt == 5:
		for i in range(N):
			result = max(result, max(cur[i]))
		return result
	new = []
	if d == 0:
		new, newCnt = toRight(cur, N, cnt)
		for d in range(4):
			result = max(result, dfs(new, newCnt, d))
	elif d == 1:
		new, newCnt = toLeft(cur, N, cnt)
		for d in range(4):
			result = max(result, dfs(new, newCnt, d))
	elif d == 2:
		new, newCnt = toUpper(cur, N, cnt)
		for d in range(4):
			result = max(result, dfs(new, newCnt, d))
	elif d == 3:
		new, newCnt = toLower(cur, N, cnt)
		for d in range(4):
			result = max(result, dfs(new, newCnt, d))
	return result

result = 0
for d in range(4):
	result = max(result, dfs(deepcopy(graph), 0, d))
print(result)