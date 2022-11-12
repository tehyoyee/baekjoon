# 3190.py

import sys
input = sys.stdin.readline
		# i  j  l  d   t
status = [1, 1, 1, 0, 0]
n = int(input())
k = int(input())
apples = [[0] * (n + 1) for _ in range(n + 1)]
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
	a, b = map(int, input().split())
	apples[a][b] = 1
l = int(input())
directions = []
for _ in range(l):
	a, b = map(str, input().split())
	directions.append([int(a), b])

k = 0
while True:
	if k < l and directions[k][0] == status[4]:
		if directions[k][1] == 'D':
			status[3] += 1
			if status[3] == 4:
				status[3] = 0
		if directions[k][1] == 'L':
			status[3] -= 1
			if status[3] == -1:
				status[3] = 3
		k += 1
	if apples[status[0]][status[1]] == 1:
		status[2] += 1
		apples[status[0]][status[1]] = 0
	graph[status[0]][status[1]] = status[4]
	if status[3] == 0:
		status[1] += 1
	elif status[3] == 1:
		status[0] += 1
	elif status[3] == 2:
		status[1] -= 1
	else:
		status[0] -= 1
	status[4] += 1
	if not (0 < status[0] <= n and 0 < status[1] <= n):
		break
	if graph[status[0]][status[1]] != 0 and graph[status[0]][status[1]] >= status[4] - status[2]:
		break
print(status[4])
