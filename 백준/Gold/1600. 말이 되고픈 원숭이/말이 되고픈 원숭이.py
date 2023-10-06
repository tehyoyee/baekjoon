# x
from collections import deque

di = [0, 0, 1, -1, 1, 2, 2, 1, -1, -2, -2, -1]
dj = [1, -1, 0, 0, 2, 1, -1, -2, -2, -1, 1, 2]

K = int(input())
W, H = map(int, input().split())
graph = []
visit = [[[0] * W for _ in range(H)] for _ in range(K + 1)]
for _ in range(H):
	graph.append(list(map(int, input().split())))

q = deque([(0, 0, 0)])
visit[0][0][0] = 1
result = -1
while q:
	ck, ci, cj = q.popleft()
	if ci == H - 1 and cj == W - 1:
		result = visit[ck][ci][cj] - 1
		break
	for k in range(4):
		ni, nj = ci + di[k], cj + dj[k]
		if 0 <= ni < H and 0 <= nj < W and graph[ni][nj] == 0:
			if visit[ck][ni][nj] == 0:
				visit[ck][ni][nj] = visit[ck][ci][cj] + 1
				q.append((ck, ni, nj))
	if ck >= K:
		continue
	for k in range(4, 12):
		ni, nj = ci + di[k], cj + dj[k]
		if 0 <= ni < H and 0 <= nj < W and graph[ni][nj] == 0:
			if visit[ck+1][ni][nj] == 0:
				visit[ck+1][ni][nj] = visit[ck][ci][cj] + 1
				q.append((ck+1, ni, nj))

print(result)