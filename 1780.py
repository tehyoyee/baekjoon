# 1780.py

import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * (n + 1)]
result = [0, 0, 0]
for _ in range(n):
	graph.append([0] + list(map(int, input().split())))

def check(i, j, l, compare):
	for y in range(i, i + l):
		for x in range(j, j + l):
			if graph[y][x] != compare:
				return False
	return True

def s(i, j, l):
	if l == 0:
		return
	if check(i, j, l, graph[i][j]):
		result[graph[i][j] + 1] += 1
		return
	else:
		l //= 3
		s(i, j, l)
		s(i, j + l, l)
		s(i, j + 2 * l, l)
		s(i + l, j, l)
		s(i + l, j + l, l)
		s(i + l, j + 2 * l, l)
		s(i + 2 * l, j, l)
		s(i + 2 * l, j + l, l)
		s(i + 2 * l, j + 2 * l, l)

s(1, 1, n)
print(result[0])
print(result[1])
print(result[2])