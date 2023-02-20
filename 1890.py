# 1890.py
# 23.02.20. 09:38 ~

di = [0, 1]
dj = [1, 0]

n = int(input())
steps = [[0] * n for _ in range(n)]
steps[0][0] = 1
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))
for i in range(n):
	for j in range(n):
		if i == n - 1 and j == n - 1:
			break
		for k in range(2):
			ni, nj = i + graph[i][j] * di[k], j + graph[i][j] * dj[k]
			if 0 <= ni < n and 0 <= nj < n:
				steps[ni][nj] += steps[i][j]
print(steps[-1][-1])