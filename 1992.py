# 1992.py

import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * (n + 1)]
for i in range(1, n + 1):
	graph.append(input().rstrip())
	graph[i] = [0] + list(map(int, graph[i]))

def check(i, j, l, compare):
	for y in range(i, i + l):
		for x in range(j, j + l):
			if graph[y][x] != compare:
				return False
	return True

def s(i, j, l, depth):
	if l == 0:
		return
	if check(i, j, l, graph[i][j]):
		print(graph[i][j], end = '')
	else:
		l //= 2
		print('(', end = '')
		s(i, j, l, depth + 1)
		s(i, j + l, l, depth + 1)
		s(i + l, j, l, depth + 1)
		s(i + l, j + l, l, depth + 1)
		print(')', end = '')
s(1, 1, n, 0)