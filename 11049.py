# 11049.py
# 23.04.17. 09:19 ~ x

import sys
input = sys.stdin.readline

def cal(a, b):
	return graph[a[0]][0] * graph[a[1]][1] * graph[b[1]][1]

N = int(input())
graph = []
for _ in range(N):
	graph.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]
for i in range(1, N):
	for j in range(N - i):
		dp[j][i + j] = min(cal([j, j + k], [j + k + 1, i + j]) + dp[j][j + k] + dp[j + k + 1][i + j] for k in range(i))
print(dp[0][N - 1])