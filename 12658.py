# 12658.py

import sys
input = sys.stdin.readline
t = int(input())

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

def check(alti_cur, i, j):
	for k in range(4):
		if 0 <= i + di[k] < h and 0 <= j + dj[k] < w:
			if alti_cur > graph[i + di[k]][j + dj[k]]:
				return True
	return False

def dfs(i, j):
	next_pos = []
	alti_cur = graph[i][j]
	next_min = 10000
	if status[i][j] != 0:
		return status[i][j]
	elif check(alti_cur, i, j):
		for k in range(4):
			if 0 <= i + di[k] < h and 0 <= j + dj[k] < w:
				next_min = min(next_min, graph[i + di[k]][j + dj[k]])
		for k in range(4):
			if 0 <= i + di[k] < h and 0 <= j + dj[k] < w:
				if next_min == graph[i + di[k]][j + dj[k]]:
					next_pos.append([i + di[k], j + dj[k]])
		return dfs(next_pos[0][0], next_pos[0][1])
	else:
		if status[i][j] == 0:
			status[i][j] = basins.pop(0)
		return status[i][j]	

for z in range(t):
	basins = []
	for i in range(26):
		basins.append(chr(ord('a') + i))
	h, w = map(int, input().split())
	status = [[0] * (w) for _ in range(h)]
	graph = []
	for _ in range(h):
		graph.append(list(map(int, input().split())))
	for i in range(h):
		for j in range(w):
			if status[i][j] == 0:
				status[i][j] = dfs(i, j)
	print("Case #%d:" %(z + 1))
	for i in range(h):
		for j in range(w):
			print(status[i][j], end = ' ')
		print()