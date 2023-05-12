# 15684.py
# 23.05.12.20:14 ~

import sys
input = sys.stdin.readline
from collections import deque

di = [0, 0, -1]
dj = [-1, 1, 0]

M, N, H = map(int, input().split())
graph = [[False] * M for _ in range(N + 1)]
for _ in range(N):
	a, b = map(int, input().split())
	graph[a][b] = True
	graph[b][a] = True

result = 4
for j in range(1, M + 1):
	visit = [[-1] * (M + 1) for _ in range(N + 1)]
	print(j)
	q = deque([[1, j, 0]])
	visit[1][j] = 0
	while q:
		ci, cj, cnt = q.popleft()
		print(ci, cj, cnt)
		if ci == N:
			result = min(result, cnt)
		for k in range(3):
			ni, nj = ci + di[k], cj + dj[k]
			if 1 <= nj and nj <= M:
				if k == 0:
					if graph[ni][nj] and cnt < visit[ni][nj]:
						visit[ni][nj] = cnt
						q.append([ni, nj, cnt])
					elif cnt < 3 and cnt + 1 < visit[ni][nj]:
						visit[ni][nj] = cnt + 1
						q.append([ni, nj, cnt + 1])
				elif k == 1:
					if graph[ci][cj] and cnt < visit[ni][nj]:
						visit[ni][nj] = cnt
						q.append([ni, nj, cnt])
					elif cnt < 3 and cnt + 1 < visit[ni][nj]:
						visit[ni][nj] = cnt + 1
						q.append([ni, nj, cnt + 1])
				else:
					if cnt < visit[ni][nj]:
						visit[ni][nj] = cnt
						q.append([ni, nj, cnt])
print(result)
						
						

					



				# if not visit[ni][nj][cnt]:
				# 	if k <= 2 and cnt < 3:
				# 		visit[ni][nj][cnt + 1] = True
				# 		q.append([ni, nj, cnt + 1])
				# 		else:
				# 			visit[ni][nj][cnt + 1] = True
				# 			q.append([ni, nj, cnt])
				# 	else:
				# 		visit[n]
