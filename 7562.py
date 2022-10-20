# 7562
# 17:50 ~ 18:16
# 19:45 ~ 21

###########################################################################

###########################################################################

import sys
input = sys.stdin.readline

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]


def to_target(cur, tar, size, visit):
	queue = [cur]
	queue[0].append(0)
	visit[cur[0]][cur[1]] = 1
	while queue:
		x, y, steps = queue.pop(0)
		if x == tar[0] and y == tar[1]:
			print(steps)
			return
		for k in range(8):
			if 0 <= x + dx[k] < size and 0 <= y + dy[k] < size and not visit[x + dx[k]][y + dy[k]]:
				queue.append([x + dx[k], y + dy[k], steps + 1])
				visit[x + dx[k]][y + dy[k]] = 1

n = int(input())
for _ in range(n):
	size = int(input())
	cur = list(map(int, input().split()))
	tar = list(map(int, input().split()))
	visit = [[0] * size for _ in range(size)]
	to_target(cur, tar, size, visit)

###########################################################################

###########################################################################

# import sys
# input = sys.stdin.readline
	  
# dx = [1, -1, -2, -2, -1, 1, 1, 2, 1, -1]
# dy = [2, 2, 1, -1, -2, -2, -1, 1, 2, 2]

# def distance_flag(x, y, tar):
# 	if abs(tar[0] - x) < 4:
# 		return 0
# 	return 1

# def set_dir(x, y, tar):
# 	if x >= tar[0]:
# 		if y <= tar[1]:
# 			return 0, 4					# 1 사분면
# 		return 2, 6						# 2
# 	else:
# 		if y >= tar[1]:					# 3
# 			return 4, 8
# 		return 6, 10					# 4

# def to_target(cur, tar, size, visit):
# 	queue = [cur]
# 	queue[0].append(0)
# 	visit[cur[0]][cur[1]] = 1
# 	while queue:
# 		x, y, steps = queue.pop(0)
# 		if x == tar[0] and y == tar[1]:
# 			print(steps)
# 			return
# 		if distance_flag(x, y, tar):
# 			i, j = set_dir(x, y, tar)
# 			for k in range(i, j):
# 				if 0 <= x + dx[k] < size and 0 <= y + dy[k] < size:
# 					queue.append([x + dx[k], y + dy[k], steps + 1])
# 		else:
# 			for k in range(8):
# 				if 0 <= x + dx[k] < size and 0 <= y + dy[k] < size and not visit[x + dx[k]][y + dy[k]]:
# 					queue.append([x + dx[k], y + dy[k], steps + 1])
# 					visit[x + dx[k]][y + dy[k]] = 1

# n = int(input())
# for _ in range(n):
# 	size = int(input())
# 	cur = list(map(int, input().split()))
# 	tar = list(map(int, input().split()))
# 	visit = [[0] * size for _ in range(size)]
# 	to_target(cur, tar, size, visit)