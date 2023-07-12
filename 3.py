# from collections import deque

# dy = [1, -1, 0, 0, -1, 1, -1, 1]
# dx = [0, 0, 1, -1, 1, 1, -1, -1]

# def is_valid(h, w, y, x):
#     return 0 <= y < h and 0 <= x < w

# def solution(board, y, x):
# 	answer = 0
# 	h = len(board)
# 	w = len(board[0])
# 	for i in range(h):
# 		board[i] = list(board[i])
# 	if board[y][x] == 'M':
# 		board[y][x] = 'X'
# 		return board
# 	visited = [[False for _ in range(w)] for _ in range(h)]
# 	dq = deque()
# 	dq.append((y, x))
# 	visited[y][x] = True
# 	while dq:
# 		y, x = dq.popleft()
# 		bomb_cnt = 0
# 		bomb_lst = []
# 		for i in range(8):
# 			ny = y + dy[i]
# 			nx = x + dx[i]
# 			if is_valid(h, w, ny, nx):
# 				bomb_lst.append((ny, nx))
# 				if board[ny][nx] == 'M':
# 					bomb_cnt += 1
# 		if bomb_cnt > 0:
# 			board[y][x] = str(bomb_cnt)
# 			bomb_lst = []
# 		else:
# 			board[y][x] = 'B'
# 			for bomb_y, bomb_x in bomb_lst:
# 				if not visited[bomb_y][bomb_x]:
# 					dq.append((bomb_y, bomb_x))
# 					visited[bomb_y][bomb_x] = True
# 	for i in range(h):
# 		for j in range(w):
# 			if board[i][j] == 'M':
# 				board[i][j] = 'E'
# 	for i in range(h):
# 		board[i] = "".join(board[i])
# 	answer = board
# 	return answer

# print(solution(["EEEEE", "EEMEE", "EEEEE", "EEEEE"], 2, 0))
# print(solution(["MME", "EEE", "EME"], 0, 0))

# from math import factorial
# for i in range(500):
# 	print(factorial(i)*factorial(i))