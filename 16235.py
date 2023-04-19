# 16235.py
# 23.04.19. 16:19 ~ x 시간초과.
# 큐에다가 나무 다 집어넣었는데, 시간초과, 2차원배열에 각각 나무를 집어넣어야하내ㅔ?

import sys
input = sys.stdin.readline
from collections import deque

di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

N, M, K = map(int, input().split())
graph = [[5] * (N + 1) for _ in range(N + 1)]
A = [[0] * (N + 1)]
trees = [[deque([]) for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(N):
	A.append([0] + list(map(int, input().split())))
for _ in range(M):
	x, y, z = map(int, input().split())
	trees[x][y].append(z)
die = deque([])
for _ in range(K):
	for i in range(1, N + 1):
		for j in range(1, N + 1):
			tmp = []
			for _ in range(len(trees[i][j])):
				cur = trees[i][j].popleft()
				if graph[i][j] >= cur:
					graph[i][j] -= cur
					trees[i][j].append(cur + 1)
				else:
					die.append([i, j, cur])
	while die:
		ci, cj, cY = die.popleft()
		graph[ci][cj] += (cY // 2)

	tmp = []
	for i in range(1, N + 1):
		for j in range(1, N + 1):
			for cur in (trees[i][j]):
				if cur % 5 == 0:
					for k in range(8):
						ni, nj = i + di[k], j + dj[k]
						if 1 <= ni <= N and 1 <= nj <= N:
							trees[ni][nj].appendleft(1)
			graph[i][j] += A[i][j]

result = 0
for i in range(N + 1):
	for j in range(N + 1):
		result += len(trees[i][j])
print(result)





# import sys
# input = sys.stdin.readline
# from collections import deque

# di = [0, -1, -1, -1, 0, 1, 1, 1]
# dj = [1, 1, 0, -1, -1, -1, 0, 1]

# N, M, K = map(int, input().split())
# graph = [[5] * (N + 1) for _ in range(N + 1)]
# A = [[0] * (N + 1)]
# trees = deque([])
# for _ in range(N):
# 	A.append([0] + list(map(int, input().split())))
# for _ in range(M):
# 	x, y, z = map(int, input().split())
# 	trees.append([z, x, y])

# die = deque([])
# for _ in range(K):
# 	for _ in range(len(trees)):
# 		cY, ci, cj = trees.popleft()
# 		if graph[ci][cj] >= cY:
# 			graph[ci][cj] -= cY
# 			trees.append([cY + 1, ci, cj])
# 		else:
# 			die.append([cY, ci , cj])
# 	while die:
# 		cy, ci, cj = die.popleft()
# 		graph[ci][cj] += (cy // 2)
# 	tmp = deque([])
# 	for cY, ci, cj in trees:
# 		if cY % 5 == 0:
# 			for k in range(8):
# 				ni, nj = ci + di[k], cj + dj[k]
# 				if 1 <= ni <= N and 1 <= nj <= N:
# 					tmp.appendleft([1, ni, nj])
# 	trees = tmp + trees
# 	for i in range(1, N + 1):
# 		for j in range(1, N + 1):
# 			graph[i][j] += A[i][j]

# print(len(trees))





# import sys
# input = sys.stdin.readline
# from collections import deque

# di = [0, -1, -1, -1, 0, 1, 1, 1]
# dj = [1, 1, 0, -1, -1, -1, 0, 1]

# N, M, K = map(int, input().split())
# graph = [[5] * (N + 1) for _ in range(N + 1)]
# A = [[0] * (N + 1)]
# trees = []
# for _ in range(N):
# 	A.append([0] + list(map(int, input().split())))
# for _ in range(M):
# 	x, y, z = map(int, input().split())
# 	heapq.heappush(trees, [z, x, y])

# year = 0
# result = M
# while year != K:
# 	tmp = []
# 	die = deque([])
# 	while trees:
# 		cY, ci, cj = heapq.heappop(trees)
# 		if graph[ci][cj] >= cY:
# 			graph[ci][cj] -= cY
# 			heapq.heappush(tmp, [cY + 1, ci, cj])
# 		else:
# 			die.append([cY, ci , cj])
# 	while die:
# 		cy, ci, cj = die.popleft()
# 		graph[ci][cj] += (cy // 2)
# 	trees = tmp
# 	tmp = deque([])
# 	for cY, ci, cj in trees:
# 		if cY % 5 == 0:
# 			for k in range(8):
# 				ni, nj = ci + di[k], cj + dj[k]
# 				if 1 <= ni <= N and 1 <= nj <= N:
# 					tmp.append([1, ni, nj])
# 	while tmp:
# 		heapq.heappush(trees, tmp.popleft())
# 	for i in range(1, N + 1):
# 		for j in range(1, N + 1):
# 			graph[i][j] += A[i][j]
# 	year += 1
	
# print(len(trees))

