# 17070.py
# 23.02.21 19:26 ~ 20:52

di = [0, 1, 1]	#가로 세로 대각선
dj = [1, 0, 1]

def is_diagonal(i, j):
	for i in range(3):
		0 <= i + di[1] < n and 0 <= j + dj[1]

def dfs(i, j, d):
	result = 0
	
	if d != 1 and 0 <= i + di[0] < n and 0 <= j + dj[0] and not visit[i + di[0]][j + dj[0]]:
		visit[i + di[0]][j + dj[0]] = True
		dfs(i + di[0], j + dj[0], 0)
		visit[i + di[0]][j + dj[0]] = False
	if d != 0 and 0 <= i + di[1] < n and 0 <= j + dj[1] and not visit[i + di[1]][j + dj[1]]:
		visit[i + di[1]][j + dj[1]] = True
		dfs(i + di[0], j + dj[0], 1)
		visit[i + di[1]][j + dj[1]] = False
			

			

n = int(input())
graph = []
visit = [[False] * n for _ in range(n)]
for _ in range(n):
	graph.append(list(map(int, input().split())))
dfs(0, 1, 0)