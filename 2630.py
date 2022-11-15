# 2630.py

import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * (n + 1)]
for _ in range(n):
	graph.append([0] + list(map(int, input().split())))
visit = [[0] * (n + 1) for _ in range(n + 1)]
white = 0
blue = 0

def s(i, j, l, color):
	if i + 1 > n or j + 1 > n:
		return
	graph[i][j] = 2
	for k in range(l + 1):
		if not 1 <= i + 1 - l <= n or not 1 <= j + 1 - l <= n:
			return
		if graph[i + 1 - k][j + 1] != color or graph[i + 1][j + 1 - k] != color:
			return
	for k in range(l + 1):
		graph[i + 1 - k][j + 1] = 2
		graph[i + 1][j + 1 - k] = 2
	s(i + 1, j + 1, l + 1, color)

for i in range(1, n + 1):
	for j in range(1, n + 1):
		if graph[i][j] != 2:
			if graph[i][j] == 0:
				white += 1
			else:
				blue += 1
			s(i, j, 1, graph[i][j])

print(white)
print(blue)