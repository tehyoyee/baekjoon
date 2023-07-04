# 17143.py
# 23.07.04. 19:55 ~

import sys
input = sys.stdin.readline
from collections import deque
				

def moveShark(i, j, s, d, R, C):
	if d == 1:
		while s > 0 and i > 1:
			i -= 1
			s -= 1
		if s > 0 and i == 0:
			return moveShark(i, j, s, 2, R, C)
	elif d == 2:
		while s > 0 and i < R:
			i += 1
			s -= 1
		if s > 0 and i == R:
			return moveShark(i, j, s, 1, R, C)
	elif d == 3:
		while s > 0 and j < C:
			j += 1
			s -= 1
		if s > 0:
			return moveShark(i, j, s, 4, R, C)
	else:
		while s > 0 and j > 1:
			j -= 1
			s -= 1
		if s > 0:
			return moveShark(i, j, s, 3, R, C)
	return i, j

result = 0
R, C, M = map(int, input().split())
sharks = deque([])
graph = [[0] * (C + 1) for _ in range(R + 1)]
# 1위 2아래 3오른쪽 4왼쪽

# r c s d z

for _ in range(M):
	r, c, s, d, z = map(int, input().split())
	if s > R * 2 + 2 and (d == 1 or d == 2):
		s %= (R * 2 - 2)
	elif s > C * 2 + 2 and (d == 3 or d == 4):
		s %= (C * 2 - 2)
	graph[r][c] = [s, d, z]


for anglerPos in range(1, C + 1):
	# catch shark
	for i in range(1, R + 1):
		if graph[i][anglerPos]:
			result += graph[i][anglerPos][2]
			graph[i][anglerPos] = 0
			break
	
	# move sharks
	nextPos = []
	for i in range(1, R + 1):
		for j in range(1, C + 1):
			if graph[i][j]:
				nextPos.append([moveShark(i, j, graph[i][j][0], graph[i][j][1], R, C), graph[i][j][0], graph[i][j][1], graph[i][j][2]])
	
	# print(nextPos)
	graph = [[0] * (C + 1) for _ in range(R + 1)]
	for (ni, nj), s, d, z in nextPos:
		if not graph[ni][nj]:
			graph[ni][nj] = [s, d, z]
		else:
			if graph[ni][nj][2] < z:
				graph[ni][nj] = [s, d, z]
	print()
	for i in range(1, R + 1):
		for j in range(1, C + 1):
			if graph[i][j]:
				print('O', end="")
			else:
				print('X', end="")
		print()






print(result)