# 10830.py
# 23.04.19. 15:00 ~ 15:50

import sys
input = sys.stdin.readline

N, B = map(int, input().split())
graph = []
dpCheck = []
dp = []

while B != 0:
	dpCheck.append(B % 2)
	B //= 2

for _ in range(N):
	graph.append(list(map(int, input().split())))
dp.append(graph)

for i in range(len(dpCheck)):
	tmp = [[0] * N for _ in range(N)]
	for i in range(N):
		for j in range(N):
			for k in range(N):
				tmp[i][j] += (graph[i][k] * graph[k][j])
			tmp[i][j] %= 1000
	graph = tmp
	dp.append(graph)
m = 0
result = [[0] * N for _ in range(N)]
for i in range(N):
	result[i][i] = 1
while m != len(dpCheck):
	if dpCheck[m] == 1:
		tmp = [[0] * N for _ in range(N)]
		for i in range(N):
			for j in range(N):
				for k in range(N):
					tmp[i][j] += (result[i][k] * dp[m][k][j])
				tmp[i][j] %= 1000
		result = tmp
	m += 1

for x in result:
	print(*x)