# 2630.py

import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * (n + 1)]
for _ in range(n):
	graph.append([0] + list(map(int, input().split())))
visit = [[0] * (n + 1) for _ in range(n + 1)]
global white 
white = 0
global blue
blue = 0

def check(i, j, l, color):
	for m in range(i, i + l):
		for n in range(j, j + l):
			if graph[m][n] != color:
				return False
	return True

def s(i, j, l):
	global white
	global blue
	if check(i, j, l, graph[i][j]):
		if graph[i][j] == 0:
			white += 1
			return
		else:
			blue += 1
			return
	else:
		l //= 2
		if l == 0:
			return
		s(i, j, l)
		s(i, j + l, l)
		s(i + l, j, l)
		s(i + l, j + l, l)
s(1, 1, n)

print(white)
print(blue)