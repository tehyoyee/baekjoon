# 1080.py
# 23.02.13 10:35 ~ 11:45?

n, m = map(int, input().split())
mat1, mat2 = [], []
graph = [[0] * m for _ in range(n)]
cnt = 0
for _ in range(n):
	mat1.append(list(map(int, input())))
for _ in range(n):
	mat2.append(list(map(int, input())))

for i in range(n):
	for j in range(m):
		graph[i][j] = mat1[i][j] == mat2[i][j]

def flip(n, m):
	for i in range(n, n + 3):
		for j in range(m, m + 3):
			graph[i][j] = abs(1 - graph[i][j])

for i in range(n - 2):
	for j in range(m - 2):
		if not graph[i][j]:
			flip(i, j)
			cnt += 1

for i in range(n):
	for j in range(m):
		if not graph[i][j]:
			print(-1)
			exit()

print(cnt)